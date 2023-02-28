from odoo import http
from odoo.http import request


class WebsiteRent(http.Controller):
    @http.route('/property/rent/<int:prop_id>', type='json', auth='public')
    def create_rent(self, prop_id, **kw):
        partner_id = request.env['res.users'].sudo().browse(request.uid).partner_id
        request.env['property.rental'].sudo().create({
                "renter_id": partner_id.id,
                "property_id": prop_id,
                "start_date": kw.get('from_date'),
            })
        return {'message': 'success'}
