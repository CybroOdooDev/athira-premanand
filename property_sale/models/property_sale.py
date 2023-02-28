from odoo import fields, models, api, _


class PropertySale(models.Model):
    _name = 'property.sale'
    _description = 'Sale of the Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'

    name = fields.Char(string='Reference', readonly=True,
                       required=True, copy=False, default='New')
    property_id = fields.Many2one('property.property', domain="[('state', '=', 'for sale')]")
    partner_id = fields.Many2one('res.partner')
    date = fields.Date("Create Date")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')], default='draft')
    invoice_ids = fields.Many2one('account.move', readonly=True)
    invoiced = fields.Boolean('Invoiced')
    sale_price = fields.Monetary("Sale Price", related='property_id.unit_price')
    book_price = fields.Monetary("Book Price", related='property_id.book_price')
    ask_price = fields.Monetary("Ask Price")
    any_broker = fields.Boolean('Any Broker')
    broker = fields.Many2one('res.partner', string="Broker")
    commission_plan_id = fields.Many2one('property.commission')
    commission_type = fields.Char(compute='_compute_commission')
    commission = fields.Monetary('Commission', compute='_compute_commission')
    broker_bill = fields.Many2one('account.move')
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id
                                  .currency_id.id,
                                  required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'property.sale') or 'New'
        res = super(PropertySale, self).create(vals)
        return res

    @api.depends('commission_plan_id', 'sale_price')
    def _compute_commission(self):
        for rec in self:
            rec.commission_type = rec.commission_plan_id.commission_type
            if rec.commission_plan_id.commission_type == 'fixed':
                rec.commission = rec.commission_plan_id.commission
            else:
                rec.commission = rec.sale_price * rec.commission_plan_id.commission / 100

    def create_invoice(self):
        self.invoiced = True
        price = self.sale_price
        if self.any_broker and self.commission:
            price -= self.commission
            self.env['property.commission.history'].create({
                'order_id': self.id,
                'partner_id': self.broker.id,
                'plan_id': self.commission_plan_id.id,
                'commission': self.commission
            })
        return {
            'name': _('Invoice'),
            'view_mode': 'form',
            'res_model': 'account.move',
            'target': 'current',
            'type': 'ir.actions.act_window',
            'context': {
                'default_move_type': 'out_invoice',
                'default_company_id': self.env.user.company_id.id,
                'default_partner_id': self.partner_id.id,
                'default_property_order_id': self.id,
                'default_invoice_line_ids': [fields.Command.create({
                    'name': self.property_id.name,
                    'price_unit': price,
                    'currency_id': self.env.user.company_id.currency_id.id
                })]
            }
        }

    def action_view_invoice(self):
        return {
            'name': _('Invoices'),
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'target': 'current',
            'type': 'ir.actions.act_window',
            'domain': [('property_order_id', '=', self.id)]
        }

    def confirm_btn(self):
        self.state = 'confirm'
        self.property_id.state = 'sold'
        self.property_id.sale_id = self.id
