from odoo import fields, models, api

class SalesItem(models.Model):
    _name = "sales_item"
    _description = "sales_item"

    name = fields.Char(compute = "rename_name") # Ini jangan ditunjukin
    item_code = fields.Char()
    item_desc = fields.Char()
    item_uom = fields.Char()
    item_tax_code = fields.Char()

    @api.depends('item_code')
    def rename_name(self):
        for i in self:
            i.name = i.item_code