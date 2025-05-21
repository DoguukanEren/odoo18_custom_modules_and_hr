from odoo import fields, models

class Employers(models.Model):
    _name = 'employers.employer'
    _description = 'Employers Info'


    name = fields.Char(string='İsim')
    employer_id = fields.Char(string='Çalışan ID')
    image = fields.Binary(string='Resim')
    birthday = fields.Date(string='Doğum Günü')
    gender = fields.Selection([
        ('female', 'Kadın'),
        ('male', 'Erkek')
    ], string='Cinsiyet')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Telefon Numarası')
    address = fields.Text(string='Addres')








