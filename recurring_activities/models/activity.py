""""Recurring Activities"""
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

from odoo import fields, models, api
import datetime


class RecurringActivity(models.Model):
    _name = 'recurring.activity'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Recurring Activity"

    name = fields.Char(string="Name")
    deadline = fields.Integer(string="Deadline in x days")
    activity = fields.Many2one('mail.activity.type')
    assigned = fields.Many2one('res.users', string="Assigned To")
    summary = fields.Char(string="Summary")
    note = fields.Char(string="Note")
    repeate_days = fields.Integer(string="Repeat Every")
    next_activity = fields.Date(string="Next Activity Date", compute='_compute_date')
    last_activity = fields.Date(string="Last Activity Date")
    interval_type = fields.Selection([('days', 'Days'), ('week', 'Week')])
    week_days = fields.Selection([('0', 'monday'), ('1', 'tuesday'), ('2', 'wednesday'), ('3', 'thursday'),
                                  ('4', 'friday'), ('5', 'saturday'), ('6', 'sunday')])

    """function used to compute dates"""
    @api.depends('repeate_days', 'week_days', 'interval_type', 'last_activity')
    def _compute_date(self):
        for item in self:
            if item.interval_type == 'days':
                item.next_activity = fields.Date.add(fields.Date.today(), days=item.repeate_days)
            elif item.interval_type == 'week':
                d = fields.Date.today()
                item.next_activity = self.next_weekday(d, int(item.week_days))
            else:
                self.next_activity = False

    """function used to create activity"""
    def activities(self):
        activity_ids = self.search([])
        for rec in activity_ids:

            if rec.next_activity == fields.Date.today():
                if rec.deadline == 0:
                    continue
                else:
                    f = self.env['mail.activity'].sudo().create({
                        'activity_type_id': rec.activity.id,
                        'date_deadline': fields.Date.today(),
                        'summary': rec.summary,
                        'user_id': rec.assigned.id,
                        'res_model_id': self.env['ir.model']._get_id('recurring.activity'),
                        'res_id': rec.id
                    })
                    rec.next_activity == rec.last_activity
                    rec.deadline = rec.deadline - 1
                    rec.last_activity = fields.Date.add(rec.next_activity, days=rec.repeate_days)

    def next_weekday(self, d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + datetime.timedelta(days_ahead)
