from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    _description = 'Quản lý thông tin sách'
    _sql_constraints = [
        ("check_book_code",'UNIQUE(book_code)', 'Mã sách tồn tại')]


    name = fields.Char("Tên sách", required=True)
    book_code = fields.Char("Mã sách", default="xxx", required=True)
    book_year_exp = fields.Char("Năm xuất bản")
    book_author = fields.Char("Tác giả")
    book_student_id = fields.Many2one('student.student', 'Student')
    book_nums_student = fields.Integer('Số lượng sinh viên mượn sách',compute='_compute_book_nums_student', store=True)

    @api.model
    def create(self, vals):
        if vals.get('book_code', 'xxx') == 'xxx':
            vals['book_code'] = self.env['ir.sequence'].next_by_code(
                'book.code.sequence')

        return super().create(vals)

    @api.depends('book_student_id')
    def _compute_book_nums_student(self):
        for record in self:
            record.book_nums_student = 1 if record.book_student_id else 0
