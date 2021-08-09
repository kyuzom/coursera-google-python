#!/usr/bin/env python3

import os
import mimetypes
import smtplib
import getpass
from email.message import EmailMessage

def generate_email(sender, recipient, subject, body, attachment_path):
	message = EmailMessage()
	message['From'] = sender
	message['To'] = recipient
	message['Subject'] = subject
	message.set_content(body)
	attachment_filename = os.path.basename(attachment_path)
	mime_type, _ = mimetypes.guess_type(attachment_path)
	mime_type, mime_subtype = mime_type.split('/', 1)
	with open(attachment_path, 'rb') as ap:
		message.add_attachment(ap.read(),
			maintype=mime_type,
			subtype=mime_subtype,
			filename=os.path.basename(attachment_path))
	return message

def send_email(sender, message):
	mail_server = smtplib.SMTP('localhost')
	mail_server.set_debuglevel(1)
	mail_server.send_message(message)

def generate_error_report(sender, recipient, subject, body):
	message = EmailMessage()
	message['From'] = sender
	message['To'] = recipient
	message['Subject'] = subject
	message.set_content(body)
	send_email(
		sender,
		message
	)

if __name__ == "__main__":
	message = generate_email(
		'automation@example.com',
		'student-01-77bddcac0cf4@example.com',
		'Upload Completed - Online Fruit Store',
		'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
		'processed.pdf'
	)
	send_email(
		'automation@example.com',
		message
	)
