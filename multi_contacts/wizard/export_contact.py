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
import base64
import io
from io import BytesIO
from odoo import fields, models, _
from odoo.exceptions import UserError
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter

try:
    import qrcode
except ImportError:
    qrcode = None


class ExportContact(models.TransientModel):
    """ExportContact class helps to print the xlsx file"""
    _name = "export.contact"
    _description = "Export Contact"

    qr_code = fields.Image(string="Image", readonly=True, help="QR Code")
    partner_ids = fields.Many2many('res.partner', string="Partner",
                                   help="you can select partners")
    xlsx_binary = fields.Binary(string='binary',
                                help="helps to add binary field")
    xlsx_binary_name = fields.Char(string="File Name", help="File Name")
    binary = fields.Boolean(string="Binary", help="Binary")

    def action_print_xlsx(self):
        """This function is used to print the xlsx report"""
        self.binary = True
        query = """select id,display_name, phone, email from res_partner
         where id in (%s)""" % (
            ','.join([str(rec) for rec in self.partner_ids.ids]))
        self.env.cr.execute(query)
        result = self.env.cr.dictfetchall()
        data = {
            'model_id': self.id,
            'result': result
        }
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'font_size': '14px'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '12px'})
        sheet.merge_range('E2:J3', 'Contact Report', head)
        sheet.write('B9', 'Sl no.', cell_format)
        sheet.merge_range('C9:E9', 'Name', cell_format)
        sheet.write('F9', 'Email', cell_format)
        sheet.write('I9', 'Phone Number', cell_format)
        count = 1
        row = 9
        col = 1
        for res in data['result']:
            sheet.write(row, col, count, txt)
            sheet.write(row, col + 1, res['display_name'], txt)
            sheet.write(row, col + 4, res['email'], txt)
            sheet.write(row, col + 7, res['phone'], txt)
            row += 1
            count = count + 1
        workbook.close()
        output.seek(0)
        xlsx = base64.b64encode(output.read())
        document_id = self.env['ir.attachment'].sudo().create({
            'name': "Contact Report",
            'type': 'binary',
            'datas': xlsx,
            'store_fname': xlsx,
        })
        self.xlsx_binary = xlsx
        if qrcode and base64:
            qr_code = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=3,
                border=4,
            )
            server_address = self.get_base_url()
            url = f"{server_address}/ir.attachment{document_id}"
            qr_code.add_data(url)
            qr_code.make(fit=True)
            img = qr_code.make_image()
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            self.update({'qr_code': qr_image})
        else:
            raise UserError(_('Necessary Requirements To Run'
                              ' This Operation Is Not Satisfied'))
        return {
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'export.contact',
            'res_id': self.id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
