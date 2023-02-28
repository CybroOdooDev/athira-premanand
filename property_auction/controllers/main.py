from odoo import http
from odoo.http import request
from odoo import fields


class WebsiteAuction(http.Controller):
    @http.route('/property/auction/', type='json', auth='public')
    def auction(self):
        auction_ids = request.env['property.auction'].sudo().search([
            ('state', '!=', 'draft')
        ])
        context = {
            'confirmed': [],
            'started': [],
            'ended': [],
        }
        for auction_id in auction_ids:
            participants = sorted(auction_id.participant_ids, key=lambda x: x.bid_amount, reverse=True)
            data = {
                'id': auction_id.id,
                'name': auction_id.property_id.name,
                'code': auction_id.auction_seq,
                'image': auction_id.property_id.image,
                'start': auction_id.start_time,
                'start_price': auction_id.bid_start_price,
                'last': participants[0].bid_amount if participants else 0,
                'end': auction_id.end_time,
                'winner': auction_id.auction_winner.name,
                'final_rate': auction_id.final_price,
                'total_participant': len(auction_id.participant_ids.ids)
            }
            if auction_id.state == 'confirmed':
                context['confirmed'].append(data)
            elif auction_id.state == 'started':
                context['started'].append(data)
            elif auction_id.state == 'ended':
                context['ended'].append(data)
        response = http.Response(template='property_auction.auction_view',
                                 qcontext=context)
        return response.render()

    @http.route('/property/auction/<int:prop_id>/bid', type='json', auth='public')
    def auction_bid_submit(self, prop_id, **kw):
        partner_id = request.env['res.users'].sudo().browse(request.uid).partner_id
        auction_id = request.env['property.auction'].sudo().search([
            ('id', '=', int(prop_id))
        ])
        auction_id.write({
            'participant_ids': [
                fields.Command.create({
                    'partner_id': partner_id.id,
                    'bid_time': fields.Datetime.now(),
                    'bid_amount': float(kw.get('bid_amount'))
                })
            ]
        })
        return {'message': 'success'}
