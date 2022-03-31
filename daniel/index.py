from pprint import pprint

data = open('index.txt', 'r').readlines()

CF = []
IUPAC = []
InChi = []

for i in list(data):
    if i[0:2] == 'CF':
        CF.append(i[4:])
    if i[0:10] == 'IUPAC Name':
        IUPAC.append(i[12:])
    if i[0:5] == 'InChI':
        InChi.append(i[7:])


molecules_full_info = []

for i in range(len(CF)):
    molecules_full_info.append(
        ['CF=' + CF[i], 'IUPAC Name=' + IUPAC[i], InChi[i]]
    )

print(molecules_full_info)


#
# data = [
#     {
#         'MF': 'C15H12AlF9O6',
#         'CF': 'Al(CF3COCHCOCH3)3',
#         'IUPAC Name': 'Aluminum Trifluoroacetylacetonate',
#         'Isomeric SMILES': 'C/C(=C\C(=O)C(F)(F)F)/O[Al](O/C(=C\C(=O)C(F)(F)F)/C)O/C(=C\C(=O)C(F)(F)F)/C ',
#         'InChI': 'InChI=1S/3C5H5F3O2.Al/c3*1-3(9)2-4(10)5(6,7)8;/h3*2,9H,1H3;/q;;;+3/p-3/b3-2+;2*3-2-; ',
#     },
#     {
#         'MF': 'C15H3AlF18O6',
#         'CF': 'Al(CF3COCHCOCF3)3',
#         'IUPAC Name': 'ALUMINUM HEXAFLUOROACETYLACETONATE',
#         'Isomeric SMILES': 'C(=C(\O[Al](O/C(=C\C(=O)C(F)(F)F)/C(F)(F)F)O/C(=C\C(=O)C(F)(F)F)/C(F)(F)F)/C(F)(F)F)\C(=O)C(F)(F)F',
#         'InChI': 'InChI=1S/3C5H2F6O2.Al/c3*6-4(7,8)2(12)1-3(13)5(9,10)11;/h3*1,12H;/q;;;+3/p-3/b3*2-1-;',
#     },
#     {
#         'MF': 'C15H21AlO6',
#         'CF': 'Al(CH3COCHCOCH3)3',
#         'IUPAC Name': 'Aluminium Acetylacetonate',
#         'Isomeric SMILES': 'C/C(=C/C(=O)C)/O[Al](O/C(=C\C(=O)C)/C)O/C(=C\C(=O)C)/C ',
#         'InChI': 'InChI=1S/3C5H8O2.Al/c3*1-4(6)3-5(2)7;/h3*3,6H,1-2H3;/q;;;+3/p-fli3/b3*4-3-;',
#     },
# ]

# CF = []
# IUPAC = []
# InChi = []

# for molecule in data:
#     CF.append(molecule['CF'])
#     IUPAC.append(molecule['IUPAC Name'])
#     InChi.append(molecule['InChI'])
