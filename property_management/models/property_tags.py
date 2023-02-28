from odoo import models, fields


class PropertyTags(models.Model):
    _name = 'property.tags'
    _description = 'Property Tags'
    _rec_name = 'tag'

    tag = fields.Char('Tag')
