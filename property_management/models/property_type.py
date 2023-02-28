from odoo import fields, models


class PropertyType(models.Model):
    _name = 'property.type'
    _description = 'Property Types'

    name = fields.Char("Name")
    type = fields.Selection([('land', "Land"),
                             ('residential', "Residential"),
                             ('commercial', "Commercial"),
                             ('industry', "Industry")], default='land')

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f'{rec.name} - {rec.type}'))
        return result

    def action_property_view(self):
        self.ensure_one()
        return {
            'name': 'Property',
            'view_mode': 'tree,form',
            'res_model': 'property.property',
            'type': 'ir.actions.act_window',
            'domain': [('type_id', '=', self.id)],
            'context': "{'create':False}"
        }
