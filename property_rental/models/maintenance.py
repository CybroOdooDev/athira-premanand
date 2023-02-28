from odoo import models, fields


class WizardMaintenance(models.Model):
    _name = 'wizard.maintenance'

    name = fields.Char(string="Name")
    property_id = fields.Many2one('property.property', string='Property', required=True)
    description = fields.Text(string="Description")
    cost = fields.Float(string="Cost")
    responsible_user_id = fields.Many2one('res.users', string="Responsible User", default=lambda
        self: self.env.user)
    stages = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled'), ('paid', 'Paid')],
        required=True, default='draft')

    def btn_cfm(self):
        self.stages = 'confirmed'

    def btn_cancel(self):
        self.stages = 'cancel'

    def btn_draft(self):
        self.stages = 'draft'

    def btn_invoice(self):
        # self.stages = 'invoiced'
        # self.write({'stages': "invoiced"})
        print(self.responsible_user_id.partner_id.id)
        invoice_id = self.env['account.move'].create({
            'move_type': 'in_invoice',
            'partner_id': self.responsible_user_id.partner_id.id,
            'date': fields.Date.today(),
            'maintenance_id': self.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [fields.Command.create({
                'name': f'{self.property_id.code} Maintenance Charge',
                'price_unit': self.cost,
            })]
        })
        self.stages = 'paid'

    def get_bill(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bill',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('maintenance_id', '=', self.id)],
        }


class Maintenance(models.Model):
    _inherit = 'account.move'

    maintenance_id = fields.Many2one('account.move')
