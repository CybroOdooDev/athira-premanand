from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class PropertyRental(models.Model):
    _name = 'property.rental'
    _description = 'Property Rent'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'code'

    property_id = fields.Many2one('property.property', string='Property', required=True,
                                  domain="[('is_rental', '=', True)]")
    code = fields.Char(string='Reference', readonly=True,
                       required=True, copy=False, default='New')
    start_date = fields.Date(string='From Date', required=True)
    end_date = fields.Date(string='Expire Date')
    rent_price = fields.Float(string='Rent/Price', related='property_id.rent_price')
    owner_id = fields.Many2one('res.partner', string='Land Lord',
                                   related='property_id.owner_id', store=True)
    renter_id = fields.Many2one('res.partner', string='Renter', required=True)
    state = fields.Selection([('draft', 'Draft'), ('in_contract', 'In Contract'),
                              ('expired', 'Expired'), ('cancel', 'Cancelled')],
                             required=True, default='draft')
    rental_bills_ids = fields.One2many('rental.bills', 'rental_id')
    payment_id = fields.Many2one('account.payment.term', string="Payment Terms")
    contract_id = fields.Many2one('property.contract')
    contract_count = fields.Integer(compute='_compute_contract_count')
    recurring_period = fields.Integer(string='Recurring Period',
                                      related='property_id.recurring_period')
    recurring_period_interval = fields.Selection([
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'),
        ('Years', 'Years'),
    ], related='property_id.recurring_period_interval')

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'property.rent') or 'New'
        res = super(PropertyRental, self).create(vals)
        res.renter_id.is_rental = True
        return res

    def _compute_contract_count(self):
        count = self.env['property.contract'].search_count([
            ('rental_id', '=', self.id)])
        self.contract_count = count

    def btn_crt_contract(self):
        if self.renter_id.rent_blacklist:
            raise ValidationError("The user is Blacklisted, "
                                  "Can not move forward with this renter.")
        self.contract_id = self.env['property.contract'].create({
            'name': self.renter_id.name + ' Contract',
            'property_id': self.property_id.id,
            'owner_id': self.owner_id.id,
            'partner_id': self.renter_id.id,
            'rent_price': self.rent_price,
            'rental_id': self.id,
            'date_start': self.start_date,
            'recurring_period': self.recurring_period,
            'recurring_period_interval': self.recurring_period_interval,
        })

    def contract_btn(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'property.contract',
            'name': 'Rental Contract',
            'view_mode': 'list,form',
            'view_type': 'form',
            'target': 'current',
            'domain': [('rental_id', '=', self.id)]
        }

    def action_maintenance(self):
        return {
            'name': 'Maintenance Request',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.maintenance',
            'view_mode': 'form',
            'context': {'default_property_id': self.property_id.id},
            'target': 'new'
        }

    def maintenance_smart_button(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Maintenance Request',
            'view_mode': 'tree,form',
            'res_model': 'wizard.maintenance',
            'domain': [('property_id', '=', self.property_id.id)],
        }


class Maintenance(models.Model):
    _inherit = 'maintenance.request'

    maintenance = fields.Boolean(default=False)


class Res(models.Model):
    _inherit = 'res.partner'

    is_rental = fields.Boolean(default=False)
