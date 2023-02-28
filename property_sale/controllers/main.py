from odoo import http
from odoo.http import request


class WebsiteSales(http.Controller):
    @http.route('/property/sale/<int:prop_id>', type='json', auth='public', csrf=False)
    def sale_submit(self, prop_id, **kw):
        partner_id = request.env['res.users'].sudo().browse(request.uid).partner_id
        property_id = request.env['property.property'].sudo().search([
            ('id', '=', int(prop_id))
        ])
        print(kw, "kww")
        print(property_id, "gggggggggg")
        sales = request.env['property.sale'].sudo().create({
                "partner_id": partner_id.id,
                "property_id": property_id.id,
                "ask_price": float(kw.get('ask_price')),
            })
        return {'message': 'success'}
