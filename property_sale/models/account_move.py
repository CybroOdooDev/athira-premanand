from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    property_order_id = fields.Many2one('property.sale')
