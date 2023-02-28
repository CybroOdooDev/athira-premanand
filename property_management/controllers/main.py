import werkzeug.utils

from odoo import http
from odoo.http import request


class MapView(http.Controller):
    @http.route('/map/<latitude>/<longitude>', type='http', auth='public')
    def redirect_map(self, latitude, longitude):
        print("hello", latitude, longitude)
        return werkzeug.utils.redirect("https://www.google.com/maps/@%s,%s,115m/data=!3m1!1e3" % (latitude, longitude))


class Website(http.Controller):
    @http.route('/property', auth='public', website=True)
    def property(self):
        property_ids = request.env['property.property'].search([])
        return request.render('property_management.property_view', {
            'property_ids': property_ids
        })


class PropertyItem(http.Controller):
    @http.route('/property/<int:property_id>', auth='public', website=True, csrf=False)
    def property_item(self, property_id):
        data = request.env['property.property'].sudo().search([('id', '=', property_id)])
        return request.render('property_management.property_view_item', {'property_id': data})
