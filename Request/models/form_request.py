from odoo import models, fields, api


class Form_request(models.Model):
    _name = 'form_request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.onchange('form_system_ids')
    def set_product_system(self):
        for system in self:
            if system.form_system_ids:
                system.form_system_product = system.form_system_ids.sys_product
                system.person_approve = system.form_system_ids.person_approve_system

    date_request = fields.Datetime(string='Thời gian thực hiện: ')
    state = fields.Selection(selection=[('submit', 'Submit'), ('confirm', 'Confirm'), ('todo', 'To do'),
                                        ('test', 'Test'), ('review', 'Review'), ('done', 'Done')], readonly=1,
                                        default='submit', track_visibility='always')
    reason_change = fields.Text(string='Lý do thay đổi')
    des_change = fields.Text(string='Mô tả thay đổi')
    before_change = fields.Text(string='Trước thay đổi')
    after_change = fields.Text(string='Sau thay đổi')
    seq_form_request = fields.Char(string='Number', require=True, readonly=True, copy=False,
                                   default=lambda self: ('New'))
    form_system_ids = fields.Many2one(comodel_name='system.request', string='System')
    # form_product_ids = fields.Many2one(comodel_name='product.request', string='Product')
    form_system_product = fields.Selection(string='Product', selection=[('nvn', 'Native Việt Nam'),
                                                                ('ntl', 'Native Thái Lan'),
                                                                ('ovn', 'OVN')], readonly=True)
    person_approve = fields.Selection(string='Approver', selection=[('thuylb3', 'Lê Biên Thùy')
                                                                    , ('hungcm', 'Chu Mạnh Hùng'),
                                                                    ('manhnv', 'Nguyễn Văn Mạnh')], readonly=True)

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

    # @api.depends('form_product_ids')
    # def set_approve_group(self):
    #     if self.person_approve:
    #         if self.form_product_ids == 'ovn':
    #             self.person_approve = 'huncm'
    #         elif self.form_product_ids == 'ntl':
    #             self.person_approve = 'manhnv'
    #         else:
    #             self.person_approve = 'thuylb3'

