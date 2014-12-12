# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp import tools


class account_invoice_line_report_logos(osv.osv):

    _name = "account.invoice.line.report_logos"
    _description = "Logos Invoices Statistics"
    _auto = False

    _columns = {
        # Estos son campos de account inovice line
        'price_unit': fields.float('Unit Price', readonly=True,),
        'price_subtotal': fields.float('Subtotal', readonly=True, group_operator="sum"),
        'quantity': fields.float('Quantity', readonly=True, group_operator="sum"),
        'discount': fields.float('Discount (%)', readonly=True),
        'price_gross_subtotal': fields.float('Gross Subtotal', readonly=True, group_operator="sum"),
        'discount_amount': fields.float('Discount Amount', readonly=True, group_operator="sum"),
        # Estos son campos de account inovice
        'period_id': fields.many2one('account.period', 'Period', readonly=True),
        'date_due': fields.date('Due Date', readonly=True),
        'number': fields.char(string='Number', size=128, readonly=True),
        #        Para otras empresas seria util agregar campos de tax
        'state': fields.selection([
            ('draft', 'Draft'),
            ('proforma', 'Pro-forma'),
            ('proforma2', 'Pro-forma'),
            ('open', 'Open'),
            ('paid', 'Done'),
            ('cancel', 'Cancelled')
        ], 'Invoice State', readonly=True),
        'date_invoice': fields.date('Date Invoice', readonly=True),
        'date_invoice_from': fields.function(lambda *a, **k: {}, method=True, type='date', string="Date Invoice from"),
        'date_invoice_to': fields.function(lambda *a, **k: {}, method=True, type='date', string="Date Invoice to"),
        'amount_total': fields.float('Invoice Total', readonly=True, group_operator="sum"),
        # Ahora llevamos de product.product
        'ean13': fields.char('EAN13', size=13, help='Barcode', readonly=True),
        'product_id': fields.many2one('product.product', 'Product', readonly=True),
        'name_template': fields.char(string="Product by text", size=128, readonly=True),
        'isbn': fields.char(string=u'ISBN', size=64, readonly=True),
        # 'type_of_product': fields.selection((('b', 'Libro'), ('d', 'DVD')), u'Tipo de producto', readonly=True),
        # Ahora llevamos de res.partner
        'partner_id': fields.many2one('res.partner', 'Partner', readonly=True),
        'customer': fields.boolean('Customer', help="Check this box if this contact is a customer.", readonly=True),
        'supplier': fields.boolean('Supplier', help="Check this box if this contact is a supplier. If it's not checked, purchase people will not see it when encoding a purchase order.", readonly=True),
        # Account journal
        'journal_id': fields.many2one('account.journal', 'Journal', readonly=True),
        # 'account_journal_name': fields.char('Journal', size=64, readonly=True),
        'type': fields.selection([
            ('out_invoice', 'Customer Invoice'),
            ('in_invoice', 'Supplier Invoice'),
            ('out_refund', 'Customer Refund'),
            ('in_refund', 'Supplier Refund'),
        ], 'Type', readonly=True),
        'user_id': fields.many2one('res.users', 'Salesman', readonly=True),
        'company_id': fields.many2one('res.company', 'Company', readonly=True),
        'editorial_id': fields.many2one('product.attribute.value', 'Editorial', domain=[('attribute_id.name', '=', 'Editorial')], readonly=True),
        'collection_id': fields.many2one('product.attribute.value', 'Collection', domain=[('attribute_id.name', '=', 'Colección')], readonly=True),
        # de res country state
        'country_id': fields.many2one('res.country', 'Country', readonly=True),
        'state_id': fields.many2one('res.country.state', 'Fed. State', readonly=True),
        'city': fields.char('City', size=64, readonly=True),
        # de product category
        'product_category_id': fields.many2one('product.category', 'Category', readonly=True),
        # 'partner_category_ids': fields.related(
        #     'partner_id',
        #     'category_id',
        #     type="many2one",
        #     relation="res.partner.category",
        #     string="Partner Category",
        #     store=False),
    }

    _order = 'id'

    def init(self, cr):

        tools.drop_view_if_exists(cr, 'account_invoice_line_report_logos')
        cr.execute("""
            CREATE OR REPLACE VIEW account_invoice_line_report_logos AS (
SELECT 
  "account_invoice_line"."id" AS "id",  
  "account_invoice_line"."price_unit" AS "price_unit",
  "account_invoice_line"."discount" AS "discount",
  case when "account_invoice"."type" in ('in_refund','out_refund') then
                         -("account_invoice_line"."quantity")
                        else
                         "account_invoice_line"."quantity"
                        end as "quantity",
  case when "account_invoice"."type" in ('in_refund','out_refund') then
                         -("account_invoice_line"."price_subtotal")
                        else
                         "account_invoice_line"."price_subtotal"
                        end as "price_subtotal",

-- Campos Calculados
  case when "account_invoice"."type" in ('in_refund','out_refund') then
                         -("price_unit" * "quantity")
                        else
                         ("price_unit" * "quantity")
                        end as "price_gross_subtotal",

  case when "account_invoice"."type" in ('in_refund','out_refund') then
                         -("price_unit" * "quantity" * ("discount"/100))
                        else
                         ("price_unit" * "quantity" * ("discount"/100))
                        end as "discount_amount",

  "account_invoice_line"."partner_id" AS "partner_id",--n
  "account_invoice_line"."product_id" AS  "product_id", --n
  
  "account_invoice"."date_due" AS "date_due",
  "account_invoice"."number" AS "number",
  "account_invoice"."journal_id" AS "journal_id",--n
  "account_invoice"."user_id" AS "user_id",--n
  "account_invoice"."company_id" AS "company_id",--n
  "account_invoice"."type" AS "type",

  "account_invoice"."state" AS "state",
  "account_invoice"."date_invoice" AS "date_invoice",

  "account_invoice"."amount_total" AS "amount_total",
  
  "product_product"."ean13" AS "ean13",
  "product_product"."name_template" AS "name_template",
  "product_template"."isbn" AS "isbn",

  "product_template"."editorial_id" AS "editorial_id", --n
  "product_template"."collection_id" AS "collection_id", --n

  "product_template"."categ_id" as "product_category_id", --n
  
  "res_partner"."customer" AS "customer",
  "res_partner"."supplier" AS "supplier",
  "res_partner"."state_id" as "state_id", --n
  "res_partner"."country_id" as "country_id", --n
  "res_partner"."city" AS "city",
  "account_invoice"."period_id" AS "period_id"

FROM "public"."account_invoice_line" "account_invoice_line"
  INNER JOIN "public"."account_invoice" "account_invoice" ON ("account_invoice_line"."invoice_id" = "account_invoice"."id")
  LEFT JOIN "public"."product_product" "product_product" ON ("account_invoice_line"."product_id" = "product_product"."id")
  INNER JOIN "public"."res_partner" "res_partner" ON ("account_invoice"."partner_id" = "res_partner"."id")
  LEFT JOIN "public"."product_template" "product_template" ON ("product_product"."product_tmpl_id" = "product_template"."id")
ORDER BY number ASC
 
        )""")
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
