from openerp import models, fields


class sale_order(models.Model):
    _inherit = "sale.order"
    buy_now = fields.Boolean('Is Buy now')
