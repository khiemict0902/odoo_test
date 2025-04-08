from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    _description = 'Quản lý thông tin sách'

    name = fields.Char("Tên sách")
    book_code = fields.Char("Mã sách", default="xxx")
    book_year_exp = fields.Integer("Năm xuất bản")
    book_author = fields.Char("Tác giả")
    book_student_id = fields.Many2one('student.student', 'Student')
    book_nums_student = fields.Integer('Số lượng sinh viên mượn sách',compute='_compute_book_nums_student', store=True)

    @api.model
    def create(self, vals):
        if vals.get('book_code', 'xxx') == 'xxx':
            book_largest_id = self.env['library.book'].search([('id','!=', '-1')]).mapped('id')
            book_largest_id = str(book_largest_id[-1]+1) if book_largest_id else '1'
            zero = 5
            count_id = '0'*(zero-len(book_largest_id)) + book_largest_id
            new_masach = 'TV'+count_id
            vals['book_code'] = new_masach
        else:
            masach = self.env['library.book'].search([('book_code','!=', '-1')]).mapped('book_code')
            if vals['book_code'] in masach:
                raise ValidationError('Mã sách tồn tại')
        return super().create(vals)

    @api.depends('book_student_id')
    def _compute_book_nums_student(self):
        for record in self:
            record.book_nums_student = 1 if record.book_student_id else 0
