from odoo import api, fields, models

class SalesContent(models.Model):
    _name = "sales_content"
    _description = "Sales Content Row"

    sales_id = fields.Many2one('sales_order')

    # Yang akan ditunjukin di tabel. :)
    item_id = fields.Many2one('sales_item')
    item_desc = fields.Char()
    quantity = fields.Integer()
    uom_code = fields.Char()
    unit_price = fields.Float()
    discount_percentage = fields.Float()
    tax_code = fields.Char()

    # Set name ketika item_no diganti (atau on save).
    @api.onchange('item_id')
    def change_name(self):
        if self.item_id.item_uom != False or self.item_id.item_uom != "":
            self.uom_code = self.item_id.item_uom
        else:
            self.uom_code = ""

        if self.item_id.item_desc != False or self.item_id.item_desc != "":
            self.item_desc = self.item_id.item_desc
        else:
            self.item_desc = ""

        if self.item_id.item_tax_code != False or self.item_id.item_tax_code != "":
            self.tax_code = self.item_id.item_tax_code
        else:
            self.tax_code = ""

    