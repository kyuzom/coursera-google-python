#!/usr/bin/env python3

import os
import requests

src='/home/student-01-77bddcac0cf4/supplier-data/images/'

url = "http://localhost/upload/"
for f in os.listdir(src):
	if not f.endswith('.jpeg'): continue
	sf = os.path.join(src, f)
	with open(sf, 'rb') as opened:
		r = requests.post(url, files={'file': opened})
