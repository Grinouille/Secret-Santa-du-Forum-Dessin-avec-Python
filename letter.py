import smtplib

import config
from santa import Santa

class Letter(object):
    def __init__(self, from_name, from_email, subject, body):
        self.from_name = from_name
        self.from_email = from_email
        self.subject = subject
        self.body = body

    def get_email_message(self, santa):
        message = \
            f'From: {self.from_name}\n' \
            f'To: {santa.recipient.name}\n' \
            f'Subject: {self.subject}\n\n' \
            f'{self.body}\n'

        message = message.replace('{santa}', santa.name)
        message = message.replace('{recipient}', santa.recipient.name)
        message = message.replace('{thème}', santa.thème)

        return message

    def send(self, santa):

        message = self.get_email_message(santa)

        try:
            server = smtplib.SMTP(config.smtp_host, config.smtp_port)
            server.starttls()
            server.login(config.smtp_user, config.smtp_pass)
            server.sendmail(self.from_email, [santa.email], message.encode('utf-8'))
            server.close()

            print('Successfully mailed letter to {}!'.format(santa.name))
        except Exception as e:
            print('Error: Failed to mail letter: {}'.format(e))
