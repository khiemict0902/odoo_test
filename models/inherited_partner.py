from odoo import fields, models, api


class StudentPartner(models.Model):
    _inherit = 'res.partner'
    # _description = 'Description'

    is_student = fields.Boolean(string='Is Student')
    student_id = fields.Many2one('student.student', string='Sinh Vien')
