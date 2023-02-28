""""Multi Contacts"""
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

from odoo import fields, models, api


class Contacts(models.Model):
    _inherit = 'res.partner'
    _description = "Multi Contacts"

    contact_ids = fields.One2many("multi.contacts", "contact_id")

    """function used to export the contacts"""
    def contact_action_export_contacts(self):
        return {
            'name': "Export Contact",
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.export',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {
                'default_partner_ids': self.env.context['active_ids']
            }
        }

    """onchange function used to set the values of fields mobile and email based on priority"""
    @api.onchange('contact_ids')
    def _onchange_contact_ids(self):
        for i in self.contact_ids:
            if i.sequence == 0:
                self.mobile = i.number
                self.email = i.email


class MultiContacts(models.Model):
    _name = "multi.contacts"

    contact_id = fields.Many2one("res.partner")
    sequence = fields.Integer(string='Sequence')
    type = fields.Char(string="Type")
    number = fields.Char(string="Number or Username")
    email = fields.Char(String="Email")
    tags_id = fields.Many2many('res.partner.category', string="Tags")
    color = fields.Integer("color")
    Note = fields.Char(string="Note")
