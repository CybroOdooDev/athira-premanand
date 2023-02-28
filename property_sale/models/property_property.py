from odoo import models, fields


class Property(models.Model):
    _inherit = 'property.property'

    sold = fields.Boolean("Is Property Sold")
    unit_price = fields.Monetary(string="Unit Price", required=True)
    sale_id = fields.Many2one('property.sale')
    state = fields.Selection(selection_add=[('for sale', 'For sale'), ('sold', 'Sold')])

    def action_property_sale_view(self):
        return {
            'name': 'Property Sale: '+self.code,
            'view_mode': 'form',
            'res_model': 'property.sale',
            'type': 'ir.actions.act_window',
            'res_id': self.sale_id.id
        }

    def to_available(self):
        self.state = 'available'

    def for_sale_btn(self):
        self.state = 'for sale'
