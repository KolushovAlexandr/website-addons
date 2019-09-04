# Copyright 2019 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import json
import logging
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


class WebsiteSaleExtended(WebsiteSale):

    def _get_search_domain(self, *args, **kwargs):
        domain = super(WebsiteSaleExtended, self)._get_search_domain(*args, **kwargs)
        company = request.website.company_id
        if not company:
            return domain
        return ['|', ('company_id', 'in', company.child_ids.ids)] + domain

    def _check_and_update_child_order(self, sale_order, product_id, product_company_id, add_qty, set_qty, **kw):
        sale_order_child = sale_order.order_child_ids.filtered(lambda so: so.company_id.id == product_company_id)
        # import wdb
        # wdb.set_trace()
        if not sale_order_child:
            sale_order_child = sale_order.sudo().create({
                'order_parent_id': sale_order.id,
                'company_id': product_company_id,
                'partner_id': sale_order.partner_id.id,
                'partner_invoice_id': sale_order.partner_invoice_id.id,
                'partner_shipping_id': sale_order.partner_shipping_id.id,
            })
            sale_order.write({
                'order_child_ids': [(4, sale_order_child.id)]
            })
            _logger.info("website_sale created new child order for company: %s for order: %s",
                         product_company_id, sale_order.id)

        if set_qty == 0 and not add_qty:
            deleted_order_lines = sale_order_child.order_line.filtered(lambda ol: ol.product_id.id == product_id)
            deleted_order_lines.unlink()
            return sale_order_child
        product_custom_attribute_values = None
        if kw.get('product_custom_attribute_values'):
            product_custom_attribute_values = json.loads(kw.get('product_custom_attribute_values'))

        no_variant_attribute_values = None
        if kw.get('no_variant_attribute_values'):
            no_variant_attribute_values = json.loads(kw.get('no_variant_attribute_values'))

        sale_order_child._cart_update(
            product_id=int(product_id),
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values
        )
        return sale_order_child

    @http.route()
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        result = super(WebsiteSaleExtended, self).cart_update(product_id, add_qty, set_qty, **kw)

        sale_order = request.website.sale_get_order()
        prod_id = request.env['product.product'].browse(int(product_id))
        product_company_id = prod_id.company_id

        if product_company_id and product_company_id != sale_order.company_id:
            self._check_and_update_child_order(sale_order, product_id, product_company_id.id, add_qty, set_qty, **kw)
        return result

    @http.route()
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):
        result = super(WebsiteSaleExtended, self).cart_update_json(product_id, line_id, add_qty, set_qty, display)

        sale_order = request.website.sale_get_order()
        prod_id = request.env['product.product'].browse(int(product_id))
        product_company_id = prod_id.company_id

        if product_company_id and product_company_id != sale_order.company_id:
            self._check_and_update_child_order(sale_order, product_id, product_company_id.id, add_qty, set_qty)
        return result
