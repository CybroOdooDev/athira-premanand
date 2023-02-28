from odoo import fields, models


class PropertyCommission(models.Model):
    _name = 'property.commission'
    _description = 'Property Commission'

    name = fields.Char('Commission Name')
    commission_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('percentage', 'Percentage')
    ])
    commission = fields.Float('Commission Rate')


class CommissionHistory(models.Model):
    _name = 'property.commission.history'

    order_id = fields.Many2one('property.sale')
    partner_id = fields.Many2one('res.partner', string="Broker")
    plan_id = fields.Many2one('property.commission')
    commission = fields.Float('Commission')

