from odoo import fields, models


class PropertyUrls(models.Model):
    _name = 'property.url'
    _description = 'Property Urls'

    name = fields.Char('Url Text')
    type = fields.Selection(selection=[('url', 'URL'), ('file', 'File')])
    url = fields.Char('Url')
    data = fields.Binary('Documents')
    property_id = fields.Many2one('property.property')
