# -*- coding: utf-8 -*-

{
    "name": "My school",
    "version": "14.0.1",
    "category": "SCOOL",
    "summary": """
        Resumé de mon module ecole
    """,
    "description": """Description du module""",
    "author": "Tdsi",
    "company": "TDSI",
    "maintainer": "Tdsi",
    "website": "https://www.tdsi.sn",
    "depends": ["base"],
    "data": [
        #"security/ir.model.access.csv",
        "data/gestion_sequences.xml",
        "views/cours_views.xml",
        "views/intervenant_views.xml",
        "views/bureau_views.xml",
        "views/specialite_views.xml",
    ],
    "installable": True,
    # 'images': ['static/description/banner.png'],
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}
