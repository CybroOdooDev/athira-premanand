from odoo.http import request
from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class WebsiteOwnersPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        user_id = request.env['res.users'].sudo().browse(request.uid)
        if 'property_count' in counters:
            print("working")
            owner_id = request.env['property.property'].sudo().search([
                ('owner_id.id', '=', user_id.partner_id.id)
            ])
            print(owner_id)
            if owner_id:
                property_count = request.env['property.property'].sudo().search_count([
                    ('owner_id.id', '=', owner_id[0].id)
                ])
            values['property_count'] = 1
        if 'commission_history_count' in counters:
            commission_history_count = request.env['property.commission.history'].sudo().search_count(
                [('partner_id.id', '=', user_id.partner_id.id)])
            values['commission_history_count'] = commission_history_count
            print(values)
        return values

    @http.route('/my/properties', website=True)
    def properties(self):
        user_id = request.env['res.users'].sudo().browse(request.uid)
        property_ids = request.env['property.property'].sudo().search([
            ('owner_id.id', '=', user_id.partner_id.id)
        ])
        print('ssss', property_ids)
        return request.render('property_management.owners_property', {
            'property_ids': property_ids,
        })
