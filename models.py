
from odoo import models, fields, api,_

class student(models.Model):



    _name = 'student.student'

    student1=fields.Char(string='student1')
    student2=fields.Char(string='student2')
    student3=fields.Char(string='student3')
    student4=fields.Char(string='student4',compute='onchange_student4',store=True)

    @api.one
    @api.depends('student1','student2','student3')
    def onchange_student4(self):
        if not self.student1 or not self.student2 or not self.student3:
            return
        self.student4=self.student1+self.student2+self.student3





