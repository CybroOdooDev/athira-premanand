# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import http
from odoo.http import request
from odoo.tools import plaintext2html


class AddMyProductReview(http.Controller):
    """Controller for adding product reviews."""
    @http.route('/add/my/review', type='json', auth='public', website=True,
                sitemap=False)
    def update_reviews(self, message, res_id, res_name, partner_id,
                       rating_count):
        """Update product reviews."""
        res_model_id = request.env['ir.model'].sudo().search(
            [('model', '=', 'product.template')]).id
        message_vals = {
            'model': 'product.template',
            'res_id': res_id,
            'record_name': res_name,
            'message_type': 'comment',
            'write_uid': partner_id,
            'body': plaintext2html(message)
        }
        request.env['mail.message'].sudo().create(message_vals)
        rec = request.env['mail.message'].sudo().search([], limit=1)
        vals = {
            'res_name': res_name,
            'res_model_id': res_model_id,
            'res_model': 'product.template',
            'res_id': res_id,
            'partner_id': partner_id,
            'feedback': message,
            'rating': rating_count,
            'consumed': True,
            'message_id': rec.id
        }
        request.env['rating.rating'].sudo().create(vals)


class DisplayDeliveryAddress(http.Controller):
    """Controller for displaying delivery address."""
    @http.route('/delivery/address', type='json', auth='public',
                website=True, sitemap=False)
    def autofill_checkout_delivery(self, add_id):
        """ Autofill the checkout delivery address."""
        partner = request.env['res.partner'].browse(add_id)
        values = {
            'name': partner.display_name,
            'street': partner.street,
            'street2': partner.street2,
            'city': partner.city,
            'state': partner.state_id.name,
            'zip': partner.zip,
            'country': partner.country_id.name,
            'email': partner.email,
            'phone': partner.phone,
            'company': partner.company_id.name
        }
        return values


class ConfirmAndUpdateDeliveryAddress(http.Controller):
    """Controller for confirming and updating delivery address."""
    @http.route('/confirm/delivery/address', type='json', auth='public',
                website=True, sitemap=False)
    def confirm_address_delivery(self, add_id):
        """ Confirm the delivery address. """
        so = request.website.sale_get_order()
        partner = request.env['res.partner'].browse(add_id)
        so.sudo().write({
            'partner_shipping_id': partner
        })

    @http.route('/update/confirm/delivery/address', type='json',
                auth='public',
                website=True, sitemap=False)
    def update_confirm_address_delivery(self, add_id, data):
        """Update and confirm the delivery address."""
        so = request.website.sale_get_order()
        partner = request.env['res.partner'].browse(add_id)
        partner.write(data)
        so.sudo().write({
            'partner_shipping_id': partner
        })


class CreateNewContactAddress(http.Controller):
    """ Controller for creating a new contact address."""
    @http.route('/create/new/ship/address', type='http', auth='public',
                website=True, sitemap=False)
    def create_new_shipping_address(self, **post):
        """Create a new shipping address."""
        uid = int(request.session['uid'])
        user = request.env['res.users'].sudo().browse(uid)
        info = {
            'name': post['new_first_name'] + post['new_last_name'],
            'parent_id': user.partner_id.id,
            'type': 'delivery',
            'street': post['new_street'],
            'country_id': int(post['new_country_id']),
            'state_id': int(post['new_state_id']),
            'street2': post['new_street2'],
            'zip': post['new_post'],
            'email': post['new_email'],
            'phone': post['new_phone']
        }
        request.env['res.partner'].sudo().create(info)
