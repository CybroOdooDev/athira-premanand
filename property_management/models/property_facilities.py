from odoo import models, fields


class PropertyFacilities(models.Model):
    _name = 'property.facilities'
    _description = 'Property Facilities'
    _rec_name = 'facility'

    facility = fields.Text('Facilities')
