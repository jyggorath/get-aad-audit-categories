#!/usr/bin/env python
from sys import argv
from sys import stderr
from requests import get


if len(argv) < 2:
	searchterm = None
else:
	searchterm = argv[1]


url = 'https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/active-directory/reports-monitoring/reference-audit-activities.md'
response = get(url)
if not response.ok:
	print('Error: GET %s => HTTP %s' % (url, response.status_code), file=stderr)
	print('Dumping response body:', file=stderr)
	print(response.text, file=stderr)
	exit(1)
markdown = response.text
markdown_lines = markdown.split('\n')


table_lines = []
for line in markdown_lines:
	if line.strip() == '':
		continue
	if line.strip().startswith('|'):
		if line.strip() != '|Audit Category|Activity|' and line.strip() != '|---|---|':
			table_lines.append(line)


for row in table_lines:
	
	cells = row.split('|')
	
	if len(cells) < 3:
		continue

	category = cells[2]

	if searchterm is not None:
		if searchterm.lower() in category.lower():
			print(category)
	else:
		print(category)

#
