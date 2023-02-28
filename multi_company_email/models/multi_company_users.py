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

from AptUrl.Helpers import _
from odoo import models, fields, api
from odoo.addons.auth_signup.models.res_partner import SignupError, now
from odoo.tools.misc import ustr


class MultiCompanyEmail(models.Model):
    _inherit = 'res.users'

    login = fields.Char(required=True, company_dependent=True, help="Used to log into the system")
    login_mail = fields.Char("Login Mail")
    signature = fields.Binary('Signature', required=True, company_dependent=True)

    def _create_user_from_template(self, values):
        template_user_id = self.env.ref(
            'base.group_user').id
        template_user = self.browse(template_user_id)
        if not template_user.exists():
            raise ValueError(_('Signup: invalid template user'))

        if not values.get('login'):
            raise ValueError(_('Signup: no login given for new user'))
        if not values.get('partner_id') and not values.get('name'):
            raise ValueError(
                _('Signup: no name or partner given for new user'))

        values['active'] = True
        try:
            with self.env.cr.savepoint():
                return template_user.with_context(no_reset_password=True).copy(
                    values)
        except Exception as e:
            raise SignupError(ustr(e))

    @api.model
    def _get_login_domain(self, login):
        return [('login_mail', '=', login)]


class Sale(models.Model):
    _inherit = 'sale.order'

    signature = fields.Binary(string="Signature", company_dependent=True)

    """function used to write the user's signature into the signature field inside the sale.order"""
    def action_confirm(self):
        if self._origin.user_id.id == self.env.uid:
            for rec in self:
                rec.write({
                    'signature': self._origin.user_id.signature,
                })
        super(Sale, self).action_confirm()
