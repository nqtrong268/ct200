from odoo import models, api, fields


class Product_request(models.Model):
    _name = 'product.request'
    _rec_name = 'name_product'

    name_product = fields.Char(string='Product')
    name_seq = fields.Char(string='Number', required=True, copy=False, readonly=True, default=lambda sefl: ('New'))
    # product_system_ids = fields.Many2one(comodel_name='system.request', string='System')
    @api.model
    def create(self, vals):
        if vals.get('name_seq', ('New')) == ('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('product.order') or ('New')
        result = super(Product_request, self).create(vals)
        return result