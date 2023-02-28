from odoo import http
from odoo.http import request


class CustomerRatingAndReview(http.Controller):
    @http.route('/final/customer_rating', type='http', auth="public", website=True, sitemap=False)
    def customer_order_rating(self, **kw):
       order_id = request.env['sale.order'].sudo().browse(int(kw['order_id']))
       order_id.comment = kw['comment']
       order_id.rating = kw['rate_value']
       return request.redirect('/shop/confirmation')
