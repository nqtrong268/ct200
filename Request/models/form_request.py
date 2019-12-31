from odoo import models, fields, api


class Form_request(models.Model):
    _name = 'form_request'

    date_request = fields.Datetime(string='Thời gian thực hiện: ')
    state = fields.Selection(selection=[('submit', 'Submit'), ('confirm', 'Confirm'), ('todo', 'To do'),
                                        ('test', 'Test'), ('review', 'Review'), ('done', 'Done')], readonly=1,
                                        default='submit')
    reason_change = fields.Text(string='Lý do thay đổi')
    des_change = fields.Text(string='Mô tả thay đổi')
    before_change = fields.Text(string='Trước thay đổi')
    after_change = fields.Text(string='Sau thay đổi')
    seq_form_request = fields.Char(string='Number', require=True, readonly=True, copy=False,
                                   default=lambda self: ('New'))
    form_system_ids = fields.Many2one(comodel_name='system.request', string='System')
    form_product_ids = fields.Many2one(comodel_name='product.request', string='Product')

    @api.model
    def create(self, vals):
        if vals.get('seq_form_request', ('New')) == ('New'):
            vals['seq_form_request'] = self.env['ir.sequence'].next_by_code('change.request.order') or ('New')
        result = super(Form_request, self).create(vals)
        return result

    @api.multi
    def change_state(self):
        if self.state == 'submit':
            self.state = 'confirm'
        elif self.state == 'confirm':
            self.state = 'todo'
        elif self.state == 'todo':
            self.state = 'test'
        else:
            self.state = 'done'

