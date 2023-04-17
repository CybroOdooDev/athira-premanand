from odoo import models, fields


class WebsiteConfigureAddress(models.TransientModel):
    _inherit = 'res.config.settings'

    phone = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.phone')
    required_phone = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.required_phone')
    street = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.street')
    street2 = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.street2')
    city = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.city')
    country = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.country')
    country_id = fields.Many2one('res.country', config_parameter='ecommerce_address_management_cybrosys.country_id')
    zip_code = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.zip_code')
    required_zip_code = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.required_zip_code')
    state = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.state')
    required_state = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.required_state')

    shipping_phone = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_phone')
    shipping_phone_required = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_phone_required')
    shipping_street = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_street')
    shipping_street_required = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_street_required')
    shipping_street2 = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_street2')
    shipping_city = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_city')
    shipping_city_required = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_city_required')
    shipping_country = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_country')
    shipping_country_id = fields.Many2one('res.country', config_parameter='ecommerce_address_management_cybrosys.shipping_country_id')
    shipping_zip_code = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_zip_code')
    shipping_zip_code_required = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_zip_code_required')
    shipping_state = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_state')
    shipping_state_required = fields.Boolean(config_parameter='ecommerce_address_management_cybrosys.shipping_state_required')
