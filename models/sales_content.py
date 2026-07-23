from odoo import api, fields, models

class SalesContent(models.Model):
    _name = "sales_content"
    _description = "Sales Content Row"

    name = fields.Char() # Ga bakal di munculin di table
    sales_id = fields.Many2one('sales_order')

    # Yang akan ditunjukin di tabel. :)
    item_no = fields.Char()
    item_desc = fields.Char()
    quantity = fields.Integer()
    uom_code = fields.Char()
    unit_price = fields.Float()
    discount_percentage = fields.Float()
    tax_code = fields.Char()

    # Set name ketika item_no diganti (atau on save).
    @api.depends('item_no')
    def change_name(self):
        for i in self:
            i.name = i.item_no