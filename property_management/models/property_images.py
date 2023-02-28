from odoo import models, fields


class PropertyImages(models.Model):
    _name = 'property.image'
    _description = 'Property Images'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    image = fields.Binary(required=True)
    property_id = fields.Many2one('property.property')
