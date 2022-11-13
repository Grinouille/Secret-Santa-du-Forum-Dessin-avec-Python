from letter import Letter
from santa import Santa

################################################################################
# SMTP configuration settings.
################################################################################
smtp_user = 'username'
smtp_pass = 'password'
smtp_host = 'email-smtp.example.com'
smtp_port = 587
from_email = 'email-used-to-send-letters@example.com'

################################################################################
# This the secret santa letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automatically replaced by the secret
# santa's name, and his/her recipient of their gift.
################################################################################
letter = Letter(
    from_name='Les orgas',
    from_email=from_email,
    subject='Secret Santa sur le Forum Dessiné',
    body="""
Cher lutin lubien connu sous le nom de {recipient}, bienvenue dans cette nouvelle session du Secret Santa.
Cette année le père Lubien te sous-traite une commande de dessin pour {santa}, avec le thème: {thème}

Festivement,
Rødkløver, Dranuki et Klariss.
"""
)

################################################################################
# The complete list of all the secret santa's and their email addresses + gift ideas.
################################################################################
santas = [
    Santa("""Cibu""","""joaquim.grimaud@gmail.com""",""" "BOSS FINAL" """),
    Santa("""Sereil""","""joaquim.grimaud@gmail.com""",""" "mon santa et moi à l'aventure (après si l'aventure c'est pas inspirant, alors carte blanche, tant qu'il y a nos deux avatars)" """),
    Santa("""Perline""","""joaquim.grimaud@gmail.com""",""" "Sous le voile de la forêt." """),
    Santa("""Myhla""","""joaquim.grimaud@gmail.com""",""" "Forêt enneigée" """),
    Santa("""Cray""","""joaquim.grimaud@gmail.com""",""" "Excursion spatiale festive entre lubiens" """),
    Santa("""Froppy""","""joaquim.grimaud@gmail.com""","""Comme dans "Oni, thunder god's tale", la série Netflix" """),
    Santa("""Toonuki""","""joaquim.grimaud@gmail.com""",""" "Pinocchio". Pas forcément le personnage, l'univers du conte en général."""),
    Santa("""Raven""","""joaquim.grimaud@gmail.com""","""patin à roulettes"""),
]

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {
    # Eviter à Raven de tomber sur les lubien.nes qui ont des personnages animaliers
    'Sereil': ('Raven',),
    'Perline': ('Raven',),
    'Froppy': ('Raven',),
    'Myhla': ('Raven',),

    # Something like below is bad, Linda can't be a secret santa for anyone!
#   'Linda': ('James', 'Mary', 'Nancy', 'John', 'Michael', 'Lisa', 'David'),
}

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
record_file = 'secret-santa-email-record.txt'
