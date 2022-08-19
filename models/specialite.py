from odoo import models, fields, api

class Specialite(models.Model):
    _name = 'gestion.specialite'
    _description = 'Une Specialite'
    _sql_constraints = [
        ('specialite_domaine_unique', 'UNIQUE(specialite, domaine)',
         'La specialite et le domaine doivent etre uniques!'),
    ]

    specialite = fields.Char(string="Spécialté", required=True)
    domaine = fields.Char(string="Domaine", required=True)

    intervenant_ids = fields.Many2many(
        'gestion.intervenant',
        string="Intervenants",
    )

