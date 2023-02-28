from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pd = fields.Boolean(string='Product Selection')

    @api.model
    def get_product_selections(self, arr):
        records = self.env['product.template'].browse(arr['product_ids'])
        if arr['checked'] == 0:
            for rec in records:
                rec.pd = True
        elif arr['checked'] == 1:
            for rec in records:
                rec.pd = False
        elif arr['checked'] == -1:
            for rec in self.env['product.template'].search([]):
                rec.pd = True
        # else:
        # for rec in self.env['product.template'].search([]):
        #     print(rec,'r')
        #     rec.pd=False
