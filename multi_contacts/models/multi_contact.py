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
import re
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MultiContact(models.Model):
    """MultiContacts class helps to set extra information for the partners"""
    _name = "multi.contact"
    _description = "Multi Contact"

    contact_id = fields.Many2one("res.partner", string="Partner",
                                 help="Partner")
    sequence = fields.Integer(string="Sequence", help="Sequence of contacts")
    type = fields.Char(string="Type", help="Contact type", required=True)
    number = fields.Char(string="Number",
                         help="Phone number of partner", required=True)
    email = fields.Char(string="Email", help="email address of partner",
                        required=True)
    tags_ids = fields.Many2many('res.partner.category', string="Tags",
                                help="type of tags")
    color = fields.Integer(string="color", help="color")
    note = fields.Char(string="Note", help="Helps to add notes")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            """function used to validate the email and phone number"""
            if vals.get('email'):
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+'
                                 '(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                 vals.get('email'))
                if match == None:
                    raise ValidationError('Not a valid E-mail ID')
            if vals.get('number'):
                match = re.match('\\+{0,1}[0-9]{10,12}', vals.get('number'))
                if match == None:
                    raise ValidationError('Invalid Phone Number')
        return super(MultiContact, self).create(vals_list)
