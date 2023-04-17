# -*- coding: utf-8 -*-
######################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Technologies (odoo@cybrosys.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#    or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
########################################################################################
from odoo import models, fields


class CrmAttachments(models.Model):
    _inherit = 'crm.lead'

    obj_attachment = fields.Integer(string='attachment',
                                    compute='_compute_obj_attachment')

    """ The Function for counting the number of attachments in CRM Lead"""

    def _compute_obj_attachment(self):
        attachment_list = []
        attachment_ids = self.env['ir.attachment'].search([
            ('res_model', '=', 'crm.lead'), ('res_id', '=', self.id)])
        if attachment_ids:
            for attachment_id in attachment_ids:
                attachment_list.append(attachment_id.id)
        self.obj_attachment = len(attachment_list)

    """This add the function for adding attachments in the CRM Lead"""

    def attach_crm(self):
        self.ensure_one()
        domain = [('res_model', '=', 'crm.lead'), ('res_id', 'in', self.ids)]
        return {

            'name': 'Attachments',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': domain,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (
                self._name, self.id)
        }
