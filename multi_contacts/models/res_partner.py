""""Multi Contacts"""
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
from odoo import api, fields, models


class ResPartner(models.Model):
    """Partner class helps to export the details of partner."""
    _inherit = 'res.partner'

    contact_ids = fields.One2many("multi.contact", "contact_id",
                                  string="Multi Contact", help="Multi Contact")

    def export_contact_action(self):
        """function used to export the contacts"""
        return {
            'name': "Export Contact",
            'type': 'ir.actions.act_window',
            'res_model': 'export.contact',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {
                'default_partner_ids': self.env.context['active_ids']
            }
        }

    @api.onchange('contact_ids')
    def _onchange_contact_ids(self):
        """onchange function used to set the values of fields mobile and email
         based on priority"""
        for rec in self.contact_ids:
            if rec.sequence == 0:
                self.mobile = rec.number
                self.email = rec.email
