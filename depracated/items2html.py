import json
from tabulate import tabulate

with open('items.json', 'r') as f:
    items = json.load(f)

table = []

first_row = ['Statement', 'NO (-2)', 'no (-1)', 'uncertain (0)', 'yes (1)', 'YES (2)']
first_row.append(' ')
first_row += ['' for _ in range(5)]

table.append(first_row)

value_format = '<pre>{:-3}' + '     </pre>'

counter = 0
for k, v in items.items():
    if counter % 4 == 0:
        table.append(['<pre> </pre>'])
    counter += 1

    row = []
    row.append(v['description'])

    row.append(' ')
    for _ in range(5):
        row.append('')
    # row.append('')

    corrs = v['correlations']

    row.append(value_format.format(int(round(corrs['o'], 1)*10)))
    row.append(value_format.format(int(round(corrs['c'], 1)*10)))
    row.append(value_format.format(int(round(corrs['e'], 1)*10)))
    row.append(value_format.format(int(round(corrs['a'], 1)*10)))
    row.append(value_format.format(int(round(corrs['n'], 1)*10)))

    table.append(row)
    # table.append([])

table.append(['<pre> </pre>'])
table.append(['<pre> </pre>'])

row = []
row.append('Final score')
table.append(row)

row = []
row.append('Divided by 20')
table.append(row)

row = []
row.append('Attribute names')
row += [' ' for _ in range(5)]
row.append(' ')
row += ['Openness', 'Conscientiousness', 'Extroversion', 'Agreeableness', 'Neuroticism']
table.append(row)

table_str = tabulate(table, headers='firstrow', tablefmt='plain')
print(table_str)

table_str = tabulate(table, tablefmt='html')
first_end = table_str.find('>')
table_str = table_str[:first_end] + ' border="1"' + table_str[first_end:]

table_str = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Self graded personality test</title>
</head>	
""" + table_str


table_str += """
<p>
When done, divide everything by 20
</p>

<p>
<ul style="list-style-type:disc">
<li> Openness (öppenhet) - att uppskatta konst, känslor, äventyr, ovanliga idéer, fantasi, nyfikenhet, och omväxlande erfarenheter. </li>
<li> Conscientiousness (samvetsgrannhet) - en tendens att vara självdisciplinerad, agera plikttroget, målinriktning; att planera snarare än att agera
spontant. </li>
<li> Extraversion - energi, positiva känslor, självsäkerhet, och en tendens att söka stimulans och andras sällskap. </li>
<li> Agreeableness (vänlighet, värme) - en tendens att vara medkännande och samarbetsvillig snarare än misstänksam och fientligt inställd mot andra.
</li>
<li> Neuroticism – tendens att lätt kunna uppleva obehagliga känslor som till exempel ilska, ångest, depression, eller sårbarhet; ibland kallad
emotionell instabilitet. </li>
</ul>
</p>
"""

with open('index.html', 'w') as f:
    f.write(table_str)
