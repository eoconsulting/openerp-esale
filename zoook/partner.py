# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2011 Zikzakmedia S.L. (http://zikzakmedia.com) All Rights Reserved.
#                       Raimon Esteve <resteve@zikzakmedia.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv, fields
from tools.translate import _
import logging

class res_partner(osv.osv):
    _inherit = "res.partner"
    _logger = logging.getLogger('zoook.res.partner')

    _columns = {
        'product_wishlist_ids':fields.many2many('product.template','partner_product_wishlist_rel','partner_id', 'product_id', 'Wishlist'),
    }

    def dj_export_manufacturers(self, cr, uid, context=None):
        """
        Return list all manufacturers
        :return [
            {'id':12, 'name':'Zikzakmedia'}
        ]
        """
        results = []
        partner_obj = self.pool.get('res.partner')

        self._logger.info("Manufacturers running")

        manufacturers = partner_obj.search(cr, uid, [('manufacturer','=',True)])
        for partner in partner_obj.browse(cr, uid, manufacturers):
            results.append({
                'id': partner.id,
                'name': partner.name,
            })

        self._logger.info("Manufacturers End")

        return results

res_partner()
