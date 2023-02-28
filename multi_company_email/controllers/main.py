""""Multi-Company Email and Signature"""
# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Technologies (<https://www.cybrosys.com>)
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
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.auth_signup.controllers.main import ensure_db, AuthSignupHome, SIGN_UP_REQUEST_PARAMS, \
    LOGIN_SUCCESSFUL_PARAMS
from odoo.http import request


class WebAuthSignup(AuthSignupHome):

    @http.route('/web/signup', type='http', auth='public', website=True,
                sitemap=False, csrf=False)
    def web_auth_signup(self, *args, **kw):
        res = super(WebAuthSignup, self).web_auth_signup(*args, **kw)
        qcontext = self.get_auth_signup_qcontext()
        if qcontext.get('login'):
            user_id = request.env['res.users'].search([('login', '=', qcontext['login'])])
            user_id.login_mail = qcontext['login']
        return res
