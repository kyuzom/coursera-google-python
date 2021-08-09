#!/usr/bin/env python3

import os
import datetime
import reports

src = '/home/student-01-77bddcac0cf4/supplier-data/descriptions/'

def get_descriptions():
	descriptions = list()
	for f in sorted(os.listdir(src)):
		sf = os.path.join(src, f)
		with open(sf, 'r') as fh:
			content = fh.readlines()
		data = {
			"name": content[0].strip(),
			"weight": int(content[1].replace('lbs', '').strip()),
			"description": content[2].strip(),
			"image_name": f.replace('.txt', '.jpeg')
		}
		descriptions.append(data)
	descriptions = sorted(descriptions, key=lambda x: x['name'])
	return descriptions

if __name__ == "__main__":
	attachment = "processed.pdf"
	title = "Processed Update on " + datetime.date.today().strftime("%B %d, %Y")
	paragraph = list()
	for data in get_descriptions():
		paragraph.append([''])
		paragraph.append(['name:', data['name']])
		paragraph.append(['weight:', str(data['weight'])+' lbs'])
	reports.generate_report(attachment, title, paragraph)
