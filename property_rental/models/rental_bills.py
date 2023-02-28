from odoo import models, fields


class RentalBills(models.Model):
    _name = 'rental.bills'
    _description = 'Rental Bills'

    bill_no = fields.Char(string='Bill Number')
    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount')
    rental_id = fields.Many2one('property.rental')
