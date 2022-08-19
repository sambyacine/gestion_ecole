from odoo import models, fields, api
from datetime import time, timedelta

class Cours(models.Model):
    _name = 'gestion.cours'
    _description = 'Un cours'
    _order = "numero"
    _sql_constraints = [
        ('annee_numero_unique', 'UNIQUE(annee, numero)',
         'L\'annee et le numero doivent etre uniques!'),
    ]

    annee = fields.Integer(string="Année", required=True)
    numero = fields.Integer(string="Numéro", required=True)
    titre = fields.Char(string="Titre")
    type = fields.Selection(
        [("Cours", "C"),
         ("TD", "TD"),
         ("TP", "TP")],
         "Type", default="Cours")
    date_debut = fields.Date(string="Date de Début")
    date_fin = fields.Date(string="Date de Fin", compute="_compute_date_fin")
    intervenant_id = fields.Many2one(
        'gestion.intervenant',
        string="Intervenant")

    @api.depends("date_debut", "date_fin")
    def _compute_date_fin(self):
        for record in self:
            if record.date_debut:
                td = timedelta(5)
                record.date_fin = record.date_debut + td
            else:
                record.date_fin = 0

    @api.model
    def create(self, values):
        values["numero"] = (
                self.env["ir.sequence"].next_by_code("gestion_cours") or "/"
        )
        print(values)
        return super(Cours, self).create(values)

    def name_get(self):
        res = []
        for record in self:
            rec_name = "%s-%s" % (record.numero, record.annee)
            res.append((record.id, rec_name))
        return res
