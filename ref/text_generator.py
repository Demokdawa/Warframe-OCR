import random

empty_list = []
count = 0

Lith_file = 'ref_lith.txt'
Meso_file = 'ref_meso.txt'
Neo_file = 'ref_neo.txt'
Axi_file = 'ref_axi.txt'
Quality_file = 'ref_quality.txt'

# Parse references files to lists
def parse_ref_files(file):
    ref_list = []
    with open(file, "r") as fileHandler:
        for line in fileHandler:
            ref_list.append(line.strip())
    return ref_list


lith_list = parse_ref_files(Lith_file)
meso_list = parse_ref_files(Meso_file)
neo_list = parse_ref_files(Neo_file)
axi_list = parse_ref_files(Axi_file)
quality_list = parse_ref_files(Quality_file)

# Parse references files to lists
def parse_ref_files(file):
    ref_list = []
    with open(file, "r") as fileHandler:
        for line in fileHandler:
            ref_list.append(line.strip())
    return ref_list

era_list = ['Lith', 'Meso', 'Neo', 'Axi']

for x in era_list:
    if x == 'Lith':
        for y in lith_list:
            z = random.choice(quality_list)
            if count + len('Relique' + x + ' ' + y + ' ' + z) < 74:
                empty_list.append('Relique ' + x + ' ' + y + ' ' + z + ' ')
            else:
                empty_list.append('\n' + 'Relique ' + x + ' ' + y + ' ' + z + ' ')
                count = len(x + ' ' + y + ' ' + z)
            count = count + len(x + ' ' + y + ' ' + z)
    if x == 'Meso':
        for y in meso_list:
            z = random.choice(quality_list)
            if count + len('Relique ' + x + ' ' + y + ' ' + z) < 74:
                empty_list.append('Relique ' + x + ' ' + y + ' ' + z + ' ')
            else:
                empty_list.append('\n' + 'Relique ' + x + ' ' + y + ' ' + z + ' ')
                count = len(x + ' ' + y + ' ' + z)
            count = count + len(x + ' ' + y + ' ' + z)
    if x == 'Neo':
        for y in neo_list:
            z = random.choice(quality_list)
            if count + len('Relique' + x + ' ' + y + ' ' + z) < 74:
                empty_list.append('Relique ' + x + ' ' + y + ' ' + z + ' ')
            else:
                empty_list.append('\n' + 'Relique ' + x + ' ' + y + ' ' + z + ' ')
                count = len(x + ' ' + y + ' ' + z)
            count = count + len(x + ' ' + y + ' ' + z)
    if x == 'Axi':
        for y in axi_list:
            z = random.choice(quality_list)
            if count + len('Relique' + x + ' ' + y + ' ' + z) < 74:
                empty_list.append('Relique ' + x + ' ' + y + ' ' + z + ' ')
            else:
                empty_list.append('\n' + 'Relique ' + x + ' ' + y + ' ' + z + ' ')
                count = len(x + ' ' + y + ' ' + z)
            count = count + len(x + ' ' + y + ' ' + z)
with open('text.txt', 'w') as f:
    for item in empty_list:
        f.write("%s" % item)