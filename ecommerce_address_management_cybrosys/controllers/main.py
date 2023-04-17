from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale



class BillingAndShipping(WebsiteSale):

    def _get_country_related_render_values(self, kw, render_values):
        '''
        This method provides fields related to the country to render the website sale form
        '''
        values = render_values['checkout']
        mode = render_values['mode']
        order = render_values['website_sale_order']

        def_country_id = order.partner_id.country_id
        # IF PUBLIC ORDER
        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
            country_code = request.geoip.get('country_code')
            if country_code:
                def_country_id = request.env['res.country'].search([('code', '=', country_code)], limit=1)
            else:
                def_country_id = request.website.user_id.sudo().country_id

        country = 'country_id' in values and values['country_id'] != '' and request.env['res.country'].search([('id','=',request.env['ir.config_parameter'].sudo().get_param('ecommerce_address_management_cybrosys.country_id'))])
        country = country and country.exists() or def_country_id


        res = {
            'country': country,
            'country_states': country.get_website_sale_states(mode=mode[1]),
            'countries': country.get_website_sale_countries(mode=mode[1]),
        }
        return res

    def _get_mandatory_fields_billing(self, country_id=False):
        zip_val = request.env['ir.config_parameter'].sudo().get_param('ecommerce_address_management_cybrosys.required_zip_code')
        state_val = request.env['ir.config_parameter'].sudo().get_param('ecommerce_address_management_cybrosys.required_state')
        print(zip_val,"zip value")
        print("this is the overrided function")
        req = ["name"]
        if country_id:
            country = request.env['res.country'].browse(country_id)
            if country.state_required:
                if state_val:
                    req += ['state_id']

            if country.zip_required:
                if zip_val:
                    req += ['zip']
        return req

    def _get_mandatory_fields_shipping(self, country_id=False):
        shipping_zip_val = request.env['ir.config_parameter'].sudo().get_param(
            'ecommerce_address_management_cybrosys.shipping_zip_code_required')
        shipping_state_val = request.env['ir.config_parameter'].sudo().get_param(
            'ecommerce_address_management_cybrosys.shipping_state_required')
        req = ["name"]
        if country_id:
            country = request.env['res.country'].browse(country_id)
            if country.state_required:
                if shipping_state_val:
                    req += ['state_id']
            if country.zip_required:
                if shipping_zip_val:
                    req += ['zip']
        return req
