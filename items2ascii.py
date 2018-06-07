import json
from tabulate import tabulate

with open('items.json', 'r') as f:
    items = json.load(f)

table = []

first_row = ['Statement', 'NO (-2)', 'no (-1)', 'uncertain (0)', 'yes (1)', 'YES (2)']
first_row.append('O')
first_row.append('C')
first_row.append('E')
first_row.append('A')
first_row.append('N')
# first_row += ['' for _ in range(5)]

table.append(first_row)

value_format = '{:-3}' + '     '

counter = 0
for k, v in items.items():
    if counter % 4 == 0:
        table.append([''])
    counter += 1

    row = []
    row.append(v['description'])

    for _ in range(5):
        row.append('')

    corrs = v['correlations']

    row.append(value_format.format(int(round(corrs['o'], 1)*10)))
    row.append(value_format.format(int(round(corrs['c'], 1)*10)))
    row.append(value_format.format(int(round(corrs['e'], 1)*10)))
    row.append(value_format.format(int(round(corrs['a'], 1)*10)))
    row.append(value_format.format(int(round(corrs['n'], 1)*10)))

    # row.append((int(round(corrs['o'], 1)*10)))
    # row.append((int(round(corrs['c'], 1)*10)))
    # row.append((int(round(corrs['e'], 1)*10)))
    # row.append((int(round(corrs['a'], 1)*10)))
    # row.append((int(round(corrs['n'], 1)*10)))

    table.append(row)
    # table.append([])

table.append([''])
table.append([''])

row = []
row.append('Final score')
table.append(row)

row = []
row.append('Divided by 20')
table.append(row)

table_str = tabulate(table, headers='firstrow', tablefmt='fancy_grid', stralign='center')
print(table_str)


table_str += """
When done, divide Final Score by 20 to get your result.

Openness (öppenhet) - att uppskatta konst, känslor, äventyr, ovanliga idéer, fantasi, nyfikenhet, och omväxlande erfarenheter. 
Conscientiousness (samvetsgrannhet) - en tendens att vara självdisciplinerad, agera plikttroget, målinriktning; att planera snarare än att agera spontant. 
Extraversion - energi, positiva känslor, självsäkerhet, och en tendens att söka stimulans och andras sällskap. 
Agreeableness (vänlighet, värme) - en tendens att vara medkännande och samarbetsvillig snarare än misstänksam och fientligt inställd mot andra.
Neuroticism – tendens att lätt kunna uppleva obehagliga känslor som till exempel ilska, ångest, depression, eller sårbarhet; ibland kallad emotionell instabilitet. 
"""

with open('ocean_test.txt', 'w') as f:
    f.write(table_str)
