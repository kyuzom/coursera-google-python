#! /usr/bin/env python3

import os
import requests

src = '/home/student-01-77bddcac0cf4/supplier-data/descriptions/'

url = "http://34.72.219.125/fruits"
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
	r = requests.post(url, json=data)
	r.raise_for_status()
