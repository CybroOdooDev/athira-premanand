from odoo import fields, models


class WizardMsg(models.TransientModel):
    _name = "wizard.msg"

    state = fields.Selection([('draft', 'Draft'), ('approval', 'Approval'), ('running', 'Running'),
                              ('expired', 'Expired'), ('closed', 'Closed'), ('to_renew', 'To Renew'),
                              ('cancelled', 'Cancelled')])
    return_reason_id = fields.Many2one('return.reason', string="Comments")

    def btn_return_for_correction(self):
        records = self.env['contract'].browse(self.env.context.get('active_ids'))
        for rec in records:
            rec.write({'state': 'draft'})

        reason = self.env['return.reason'].browse(self.env.context.get('active_ids'))
        for rec in reason:
            rec.write({'name': self.return_reason_id})

