from odoo import models, fields


class ContactsBlacklist(models.Model):
    _inherit = 'res.partner'

    rent_blacklist = fields.Boolean(string='Is Blacklist', default=False)

    def add_to_blacklist(self):
        print('ss')
        self.rent_blacklist = True

    def remove_blacklist(self):
        self.rent_blacklist = False
