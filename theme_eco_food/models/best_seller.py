from odoo import fields, models


class BestSeller(models.Model):
    _name = "dynamic.products"
    _description = "Best Seller"

    name = fields.Char(string="Name")
    product_tmpl_ids = fields.Many2many('product.template')
