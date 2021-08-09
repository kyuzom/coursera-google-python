#!/usr/bin/env python3

import os
from PIL import Image, UnidentifiedImageError

src='/home/student-01-77bddcac0cf4/supplier-data/images/'
dst='/home/student-01-77bddcac0cf4/supplier-data/images/'

for f in os.listdir(src):
	sf = os.path.join(src, f)
	nf = os.path.join(dst, f.replace('.tiff', '.jpeg'))
	try:
		im = Image.open(sf).convert('RGB').resize((600, 400))
	except UnidentifiedImageError:
		continue
	else:
		im.save(nf)
