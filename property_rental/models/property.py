from odoo import models, fields


class PropertyRentalDetails(models.Model):
    _inherit = 'property.property'

    is_rental = fields.Boolean(string='For Rental', default=False)
    state = fields.Selection(selection_add=[('for_rent', 'For Rent'), ('sold', 'Sold')])
    rent_price = fields.Float(string='Rent Price')
    rental_history = fields.One2many('property.rental', 'property_id')
    recurring_period = fields.Integer(string='Recurring Period')
    recurring_period_interval = fields.Selection([
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('Months', 'Months'),
        ('Years', 'Years'),
    ], )

    def btn_available(self):
        self.is_rental = False
        self.state = 'available'

    def for_rent_btn(self):
        self.is_rental = True
        self.state = 'for_rent'
