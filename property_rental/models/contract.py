from odoo import models, fields, api
from odoo.tools import date_utils


class PropertyContract(models.Model):
    _name = 'property.contract'
    _description = 'Property Contract'

    name = fields.Char(string='Contract Name', required=True, )
    partner_id = fields.Many2one('res.partner', string="Renter")
    recurring_period = fields.Integer(string='Recurring Period')
    recurring_period_interval = fields.Selection([
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'),
        ('Years', 'Years'),
    ], )
    property_id = fields.Many2one('property.property', required=True)
    owner_id = fields.Many2one('res.partner', required=True)
    rent_price = fields.Float(string='Rent Price')
    rental_id = fields.Many2one('property.rental')
    contract_reminder = fields.Integer(
        string='Contract Expiration Reminder (Days)')
    recurring_invoice = fields.Integer(
        string='Recurring Invoice Interval (Days)')
    next_invoice = fields.Date(string='Next Invoice Date', store=True,
                               compute='_compute_next_invoice')
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Currency')
    date_start = fields.Date(string='Start Date')
    invoice_count = fields.Integer(store=True,
                                   compute='_compute_invoice_count')
    date_end = fields.Date(string='End Date')
    lock = fields.Boolean()
    state = fields.Selection([
        ('New', 'New'),
        ('Ongoing', 'Ongoing'),
        ('Expire Soon', 'Expire Soon'),
        ('Expired', 'Expired'),
        ('Cancelled', 'Cancelled'),
    ], string='Stage', default='New', copy=False, required=True, tracking=True,
        readonly=True)
    note = fields.Html(string="Terms and conditions", translate=True)

    def button_to_confirm(self):
        self.write({'state': 'Ongoing'})

    def button_to_cancel(self):
        self.write({'state': 'Cancelled'})

    def button_to_generate_invoice(self):
        data = self.env['account.move'].create([
            {
                'move_type': 'out_invoice',
                'partner_id': self.partner_id.id,
                'invoice_date': fields.date.today(),
                'contract_id': self.id,
                'invoice_line_ids': [(0, 0, {
                    'name': self.property_id.name,
                    'quantity': 1,
                    'price_unit': self.rent_price,
                })],

            }])
        self.invoice_count = self.env['account.move'].search_count([
            ('contract_id', '=', self.id)])

    def button_to_lock(self):
        self.lock = True

    def button_to_unlock(self):
        self.lock = False

    def get_invoice(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('contract_id', '=', self.id)],
        }

    @api.depends('partner_id')
    def _compute_invoice_count(self):
        self.invoice_count = self.env['account.move'].search_count([
            ('contract_id', '=', self.id)
        ])

    @api.depends('date_start', 'recurring_invoice', 'recurring_period',
                 'recurring_period_interval')
    def _compute_next_invoice(self):
        self.next_invoice = fields.Date.today()
        start_date = self.date_start
        interval = self.recurring_invoice
        recurring_period = self.recurring_period
        recurring_period_interval = self.recurring_period_interval
        self.next_invoice = date_utils.add(start_date,
                                           days=int(interval))
        if recurring_period_interval == 'Days':
            next_schedule = date_utils.add(start_date,
                                           days=int(recurring_period))
            self.date_end = next_schedule
        elif recurring_period_interval == 'Weeks':
            next_schedule = date_utils.add(start_date,
                                           weeks=int(recurring_period))
            self.date_end = next_schedule
        elif recurring_period_interval == 'Months':
            next_schedule = date_utils.add(start_date,
                                           months=int(recurring_period))
            self.date_end = next_schedule
        else:
            next_schedule = date_utils.add(start_date,
                                           years=int(recurring_period))
            self.date_end = next_schedule

    @api.model
    def property_contract_state_change(self):
        records = self.env['property.contract'].search([])
        for rec in records:
            end_date = rec.date_end
            expiry_reminder = rec.contract_reminder
            expiry_warning_date = date_utils.subtract(end_date, days=int(expiry_reminder))
            current_date = fields.Date.today()
            next_invoice = rec.next_invoice

            if expiry_warning_date <= current_date <= end_date:
                rec.write({'state': 'Expire Soon'})
            if end_date < current_date:
                rec.write({'state': 'Expired'})

            if next_invoice == current_date and rec.state != 'Cancelled':
                data = rec.env['account.move'].create([
                    {
                        'move_type': 'out_invoice',
                        'partner_id': self.partner_id.id,
                        'invoice_date': fields.date.today(),
                        'contract_id': self.id,
                        'invoice_line_ids': [(0, 0, {
                            'name': self.property_id.name,
                            'quantity': 1,
                            'price_unit': self.rent_price,
                        })],
                    }])
                rec.invoice_count = rec.env['account.move'].search_count([
                    ('contract_id', '=', rec.id)
                ])


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    contract_id = fields.Integer(string='Property Contract ')









