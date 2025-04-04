from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    # _description = 'Description'

    name = fields.Char("Ten sach")
    book_masach = fields.Char("Ma sach", default="xxx")
    book_year_exp = fields.Integer("Nam xuat ban")
    book_author = fields.Char("Tac gia")
    book_student_id = fields.Many2one('student.student', 'Student')
    so_luong_sv = fields.Integer('So luong sinh vien muon sach',compute='_compute_so_luong_sv', store=True)

    @api.model
    def create(self, vals):
        if vals.get('book_masach', 'xxx') == 'xxx':
            book_largest_id = self.env['library.book'].search([('id','!=', '-1')]).mapped('id')
            book_largest_id = str(book_largest_id[-1]+1) if book_largest_id else '1'
            zero = 5
            count_id = '0'*(zero-len(book_largest_id)) + book_largest_id
            new_masach = 'TV'+count_id
            vals['book_masach'] = new_masach
        else:
            masach = self.env['library.book'].search([('book_masach','!=', '-1')]).mapped('book_masach')
            if vals['book_masach'] in masach:
                raise ValidationError('Ma sach ton tai')
        return super().create(vals)

    @api.depends('book_student_id')
    def _compute_so_luong_sv(self):
        for record in self:
            record.so_luong_sv = 1 if record.book_student_id else 0
