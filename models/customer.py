from odoo import fields, models

class SalesCustomer(models.Model):
    _name = "sales_customer"
    _description = "Sales Customer"

    name = fields.Char()
    customer_information = fields.Text()
    