#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
	report = SimpleDocTemplate(attachment)
	styles = getSampleStyleSheet()
	report_title = Paragraph(title, styles["h1"])
	table_style = [('GRID', (0,0), (-1,-1), 1, colors.white)]
	report_table = Table(data=paragraph, style=table_style, hAlign="LEFT")
	report.build([report_title, report_table])
