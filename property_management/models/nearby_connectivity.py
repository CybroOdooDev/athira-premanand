from odoo import fields, models


class NearbyConnectivity(models.Model):
    _name = 'property.nearby.connectivity'
    _description = 'Property Nearby Connectivity'

    name = fields.Char(string="Name")
    kilometer = fields.Float(string="Kilometer")
    property_line_id = fields.Many2one('property.property')
