from odoo import fields, models


class PropertySaleReport(models.TransientModel):
    _name = 'property.sale.report'

    from_date = fields.Date("From Date")
    to_date = fields.Date("To Date")
    property_id = fields.Many2one('property.property', string="Property Name")
    partner_id = fields.Many2one('res.partner', string="Customer")

    def action_create_report(self):
        query = """ select a.name as customer,b.name,x.create_date,x.state from property_sale x
                                    join res_partner a on partner_id = a.id 
                                    join property_property b on x.property_id = b.id"""
        if self.partner_id:
            partner_id = """ and a.name = '%s'""" % self.partner_id.name
            query += partner_id
        if self.property_id:
            property_id = """ and b.name = '%s'""" % self.property_id.name
            query += property_id
        if self.from_date:
            date_query = """ and create_date > '%s'""" % self.from_date
            query += date_query
        if self.to_date:
            date_query = """ and create_date < '%s'""" % self.to_date
            query += date_query
        self._cr.execute(query)
        datas = self.env.cr.dictfetchall()
        print(datas)
        data = {
            'datas': datas,
            'to_date': self.to_date,
            'from_date': self.from_date,
            'partner_name': self.partner_id.name,
            'property_name': self.property_id.name,
        }
        return self.env.ref('property_sale.action_property_sale_report').report_action(self, data=data)
