from odoo import fields, models, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'Quản lý thông tin sinh viên'
    _rec_name = 'stu_display_name'
    _sql_constraints = [
        ("check_stu_code", "UNIQUE(stu_code)", "Mã sinh viên đã tồn tại, vui lòng nhập mã sinh viên khác!"),
    ]

    stu_name = fields.Char('Tên sinh viên')
    stu_code = fields.Char('Mã sinh viên')
    stu_display_name = fields.Char('Tên hiển thị', readonly=True, compute='_compute_stu_display_name')
    stu_birth_date = fields.Date('Ngày sinh')
    stu_email = fields.Char('Email')
    stu_phone = fields.Char('Số điện thoại')

    contact_ids = fields.One2many('res.partner', 'student_id', "Liên hệ")
    book_ids = fields.One2many("library.book", "book_student_id", "Sách", readonly=True)

    stu_nums_book =fields.Char('Số lượng sách', compute='_compute_book_count', store=True)

    @api.depends('stu_name', 'stu_code')
    def _compute_stu_display_name(self):
        for record in self:
            if record.stu_code != False and  record.stu_code != False:
                record.stu_display_name = str(record.stu_code) + '-' + str(record.stu_name)
            else:
                record.stu_display_name = ''
    @api.depends('book_ids')
    def _compute_book_count(self):
        for record in self:
            book_number = len(record.mapped('book_ids.id'))
            record.stu_nums_book = str(book_number)
