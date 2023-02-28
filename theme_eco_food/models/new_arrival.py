from odoo import fields, models


class FeaturedProducts(models.Model):
    _name = "new.arrival"
    _description = "New Arrival Products"

    name = fields.Char(string="Name")
    new_arrivals_ids = fields.Many2many('product.template')
