from odoo import api, fields, models

class SalesOrder(models.Model):
    _name = "sales_order"
    _description = "Sales Order Main"

    # ---------- Informasi Di Header
    name = fields.Char(compute = "set_sales_name") # JANGAN TUNJUKIN INI, buat @api.depends('sales_id') untuk set name
    sales_id = fields.Char()
    customer_id = fields.Many2one('sales_customer')
    contact_person = fields.Many2one('sales_contact')
    customer_ref_no = fields.Char()
    currency = fields.Char()
    
    sales_order_number = fields.Char()
    sales_order_status = fields.Selection(
        string = "Item or Service", 
        selection =  [('status_open', 'Open'), ('status_closed', 'Closed'), ('status_cancelled', 'Cancelled')]
    )
    
    posting_date = fields.Date()
    delivery_date = fields.Date()
    document_date = fields.Date()

    # ------------- Informasi Kolom Contents
    item_or_service_type = fields.Selection(
        string = "Item or Service",
        selection = [('type_item', 'Item'), ('type_service', 'Service')],
        help = "Tentukan jenis"
    )
    summary_type = fields.Selection(
            string = "Summary Type",
            selection = [('st_summary', 'Summary'), ('st_none', 'No Summary')],
            help = "Tentukan jenis"
        )
    sales_contents = fields.One2many(comodel_name = "sales_content", inverse_name = "sales_id")
    # Ini bakal pake List dengan fields.One2many(comodel_name = "po_content", inverse_name = "po_id")

    # ------------- Informasi Logistics
    shipping_location = fields.Many2one('ship_location')
    payment_info = fields.Many2one('payment_info')
    ship_ta = fields.Text()
    pay_ta = fields.Text()

    shipping_type = fields.Many2one('shipping_type')
    bp_channel_name = fields.Char()
    bp_channel_contact = fields.Many2one('res.partner')

    # -------------- Accounting
    journal_remark = fields.Char()
    payment_term = fields.Selection(
        string = "Payment Term",
        selection = [('pay_cash', 'Cash'), ('pay_bank', 'bank')],
        help = "Payment term here.."
    ) 
    payment_method = fields.Selection(
        string = "Payment Method",
        selection = [('pm_1', 'method 1'), ('pm_2', 'method 2')],
        help = "Payment Method here.."
    )
    due_date = fields.Date()
    bp_project = fields.Char()
    cancellation_date = fields.Date()
    required_date = fields.Date()
    indicator = fields.Char()
    tax_id = fields.Char()
    order_number = fields.Char()

    # ------------- Attachments
    att_attachment = fields.Many2many(comodel_name="ir.attachment")

    @api.depends('sales_id')
    def set_sales_name(self):
        for i in self:
            i.name = i.sales_id

    # Autofill customer reference number apabila dia ada. 
    @api.onchange('customer_id')
    def autoset_customer_ref_no(self):
        # Memeriksa apakah customer_id itu diisi ato tidak customer_ref_no
        if self.customer_id.customer_ref_no != False or self.customer_id.customer_ref_no != "":
            # Masukan customer_ref_no pada self apabila customer_ref_no milik customer_id terisi.
            self.customer_ref_no = self.customer_id.customer_ref_no
        else:
            self.customer_ref_no = ""


    # Autofill di kotak di kanan shipping location Many2one
    @api.onchange('shipping_location')
    def set_ship_ta(self):
        if self.shipping_location:
            self.ship_ta = str(self.shipping_location.shipping_location)
        else:
            self.ship_ta = ""

    # Autofill di kotak di kanan payment info Many2one
    @api.onchange('payment_info')
    def set_pay_ta(self):
        if self.payment_info:
            self.pay_ta = str(self.payment_info.payment_details)
        else:
            self.pay_ta = ""

    def do_nothing(self):
        return