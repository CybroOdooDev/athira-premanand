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
from odoo import http
from odoo.http import request


class MarsPortfolio(http.Controller):
    """Controller class for handling Mars portfolio related requests."""
    @http.route('/portfolio', type='http', auth='public', website=True,
                sitemap=False)
    def portfolio(self):
        """Renders the Mars portfolio page."""
        headings = request.env['mars.portfolio'].search([])
        portfolio = []
        for headings in headings:
            portfolio.append(headings)
        values = {
            'heading': portfolio,
            'my_heading': portfolio,
        }
        return request.render("theme_mars.mars_portfolio", values)
