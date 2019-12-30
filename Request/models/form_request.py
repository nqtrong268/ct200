from odoo import models, fields, api


class Form_request(models.Model):
    _name = 'form_request'

    date_request = fields.Datetime(string='Thời gian thực hiện: ')
    state = fields.Selection(selection=[('submit', 'Submit'), ('confirm', 'Confirm'), ('todo', 'To do'),
                                        ('test', 'Test'), ('review', 'Review'), ('done', 'Done')])
    reason_change = fields.Text(string='Lý do thay đổi')
    des_change = fields.Text(string='Mô tả thay đổi')
    before_change = fields.Text(string='Trước thay đổi')
    after_change = fields.Text(string='Sau thay đổi')
