from odoo import models, fields, api

class Bureau(models.Model):
    _name = 'gestion.bureau'
    _description = 'Un bureau'
    _order = 'NumBureau'
    _sql_constraints = [
        ('numBureau_batiment_centre_unique', 'UNIQUE(nunBureau, batiment, centre)',
         'Le numéro du bureau, le batiment et le centre doivent etre uniques!'),
    ]

    numBureau = fields.Integer(string="Numéro du Bureau", required=True)
    batiment = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'),('D', 'D'),('E', 'E'),('F', 'F'),('G', 'G'),
                                 ('H', 'H'),('I', 'I'),('J', 'J'),('K', 'K'),('L', 'L'),('M', 'M'),('N', 'N'),('O', 'O'),
                                 ('P', 'P'),('Q', 'Q'),('R', 'R'),('S', 'S'),('T', 'T'),('U', 'U'),('V', 'V'),('W', 'W'),
                                 ('X', 'X'),('Y', 'Y'),('Z', 'Z')],
                                'Bâtiment', default='A')
    centre = fields.Selection([('Royallieu', 'R'),('Benjamin Franklin', 'BF'),('Pierre Guillaumat', 'PG')],
                              'Centre', default='Royallieu')
    intervenant_ids = fields.One2many(
        'gestion.intervenant',
        'bureau_id',
        'Intervenants')

    def name_get(self):
        res = []
        for record in self:
            rec_name = "%s-%s" % (record.numBureau, batiment)
            res.append((record.id, rec_name))
        return res