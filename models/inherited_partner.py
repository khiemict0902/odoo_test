from odoo import fields, models, api


class StudentPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Liên hệ sinh viên'

    is_student = fields.Boolean(string='Là sinh viên')
    student_id = fields.Many2one('student.student', string='Sinh viên')
