from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    rental_reminder = fields.Boolean(config_parameter='property_rental.rental_reminder', default=False)
    rental_reminder_days = fields.Integer(config_parameter='property_rental.rental_reminder_days')
    rental_follow_up = fields.Boolean(config_parameter='property_rental.rental_follow_up', default=False)
    rental_follow_up_days = fields.Integer(config_parameter='property_rental.rental_follow_up_days')
