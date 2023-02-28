from odoo import fields, models


class NeighboursData(models.Model):
    _name = 'neighbours.data'
    _description = 'Neighbours Data'

    name = fields.Char(string="Name")
    phone_number = fields.Char(string="Phone Number")
    address = fields.Text(string="Address")
    direction = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'),   ('west', 'West')])
    neighbours_line_id = fields.Many2one('property.property')
