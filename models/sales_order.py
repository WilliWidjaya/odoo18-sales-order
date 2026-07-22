from odoo import api, fields, models

class SalesOrder(models.Model):
    _name = "sales_order"
    _description = "Sales Order Main"

    name = fields.Char()
    customer_id = fields.Char()
    contact_person = fields.Many2one('res.partner')
    customer_ref_no = fields.Char()
    currency = fields.Char()