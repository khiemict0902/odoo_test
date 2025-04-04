from odoo import fields, models, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'Description'
    _rec_name = 'stu_ten_hien_thi'
    _sql_constraints = [
        ("check_stu_id", "UNIQUE(stu_id)", "Mã sinh viên đã tồn tại, vui lòng nhập mã sinh viên khác!"),
    ]

    stu_name = fields.Char('Tên Sinh Viên')
    stu_id = fields.Char('Ma Sinh Viên')
    stu_ten_hien_thi = fields.Char('Tên hien thi', readonly=True, compute='_compute_stu_ten_hien_thi')
    stu_ngay_sinh = fields.Date('Ngay sinh')
    stu_email = fields.Char('Email')
    stu_sdt = fields.Char('So dien thoai')

    lien_he_ids = fields.One2many('res.partner', 'student_id', "Lien he")
    book_ids = fields.One2many("library.book", "book_student_id", "Sach", readonly=True)

    so_luong_sach =fields.Char('So luong sach', compute='_compute_book_count', store=True)

    @api.depends('stu_name', 'stu_id')
    def _compute_stu_ten_hien_thi(self):
        for record in self:
            if record.stu_id != False and  record.stu_id != False:
                record.stu_ten_hien_thi = str(record.stu_id) + '-' + str(record.stu_name)
            else:
                record.stu_ten_hien_thi = ''
    @api.depends('book_ids')
    def _compute_book_count(self):
        for record in self:
            book_number = len(record.mapped('book_ids.id'))
            record.so_luong_sach = str(book_number)
