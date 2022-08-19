from odoo import models, fields, api

class Intervenant(models.Model):
    _name = 'gestion.intervenant'
    _description = 'Un intervenant'
    _order = 'nom'
    _sql_constraints = [
        ('nom_unique', 'UNIQUE(nom)',
         'Le nom doit etre unique!'),
    ]

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom")
    telephone1 = fields.Integer(string="Telephone")
    telephone2 = fields.Integer(string="Autre Telephone")
    telephone3 = fields.Integer(string="Autre Telephone")

    cours_ids = fields.One2many(
        'gestion.cours',
        'intervenant_id',
        string="Cours")
    bureau_id = fields.Many2one(
        'gestion.bureau',
        string='Bureau',
    )
    specialite_ids = fields.Many2many(
        'gestion.specialite',
        string="Spécialités",
    )

    def name_get(self):
        res = []
        for record in self:
            rec_name = "%s-%s" % (record.nom, record.prenom)
            res.append((record.id, rec_name))
        return res