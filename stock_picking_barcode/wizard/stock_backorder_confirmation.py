# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class StockPickingBackorderConfirmation(models.TransientModel):
    _inherit = 'stock.backorder.confirmation'

    @api.one
    def put_in_cart(self, picking_ids):
        processed_ids = []
        for operation in self.env["stock.picking"].browse(picking_ids).move_line_ids:
            if operation.qty_done and not operation.processed and operation.qty_done <= operation.product_qty:
                op = operation.copy({'product_uom_qty': operation.qty_done, 'qty_done': operation.qty_done})
                operation.write({'product_uom_qty': operation.product_qty - operation.qty_done, 'qty_done': 0})
                processed_ids.append(op.id)
            self.env["stock.move.line"].browse(processed_ids).write({'processed': True})
