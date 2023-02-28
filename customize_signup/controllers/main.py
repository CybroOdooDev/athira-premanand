# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
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

from odoo import http, tools, _
import base64
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.auth_signup.controllers.main import ensure_db, AuthSignupHome, SIGN_UP_REQUEST_PARAMS, \
    LOGIN_SUCCESSFUL_PARAMS
from odoo.http import request


class WebAuthSignup(AuthSignupHome):
    """function used to add extra information at the time of signup"""
    @http.route('/web/signup', type='http', auth='public', website=True,
                sitemap=False, csrf=False)
    def web_auth_signup(self, *args, **kw):
        res = super(WebAuthSignup, self).web_auth_signup(*args, **kw)
        qcontext = self.get_auth_signup_qcontext()
        User = request.env['res.users']
        user_sudo = User.sudo().search(
            User._get_login_domain(qcontext.get('login')), order=User._get_login_order(), limit=1
        )
        if 'file' in kw:
            data_b64 = kw['file']
            data = base64.b64encode(data_b64.read()) if data_b64 else b''
            user_sudo.partner_id.image_1920 = data
        if 'mobile' in kw:
            user_sudo.partner_id.mobile = kw['mobile']
        if 'job_position' in kw:
            user_sudo.partner_id.function = kw['job_position']
        if 'country' in kw:
            country = request.env['res.country'].search([('id', '=', kw['country'])])
            user_sudo.partner_id.country_id = country
        return res
