#!/usr/bin/env python3

import psutil
import socket
import emails

def check_cpu_usage():
	return psutil.cpu_percent(interval = 0.5) > 80

def check_available_disk_space():
	return psutil.disk_usage('/').percent > 80

def check_available_memory():
	try:
		return psutil.virtual_memory('/')[4] < 500000000
	except Exception:
		return False

def check_hostname_resolve():
	try:
		socket.gethostbyname('localhost')
	except Exception:
		return True
	else:
		return False

if __name__ == "__main__":
	if check_cpu_usage():
		emails.generate_error_report(
			'automation@example.com',
			'student-01-77bddcac0cf4@example.com',
			'Error - CPU usage is over 80%',
			'Please check your system and resolve the issue as soon as possible.'
		)
	if check_available_disk_space():
		emails.generate_error_report(
			'automation@example.com',
			'student-01-77bddcac0cf4@example.com',
			'Error - Available disk space is less than 20%',
			'Please check your system and resolve the issue as soon as possible.'
		)
	if check_available_memory():
		emails.generate_error_report(
			'automation@example.com',
			'student-01-77bddcac0cf4@example.com',
			'Error - Available memory is less than 500MB',
			'Please check your system and resolve the issue as soon as possible.'
		)
	if check_hostname_resolve():
		emails.generate_error_report(
			'automation@example.com',
			'student-01-77bddcac0cf4@example.com',
			'Error - localhost cannot be resolved to 127.0.0.1',
			'Please check your system and resolve the issue as soon as possible.'
		)
