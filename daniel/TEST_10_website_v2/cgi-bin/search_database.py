#!/usr/bin/python3

# Read in the environment variable created by HTML

import os
import pickle
from urllib.parse import unquote

GET = {}
args = os.getenv("QUERY_STRING").split('&')

for arg in args:
	t = arg.split('=')
	if len(t) > 1:
		kkey = arg.split('=')[0]
		vvalue = arg.split('=')[1]
		vvalue = vvalue.replace('+',' ')
		vvalue = unquote(vvalue)
		GET[kkey] = vvalue

# Get data from fields
MF = GET['MF']
CF = GET['CF']
IUPAC_Name = GET['IUPAC_Name']
InChI = GET['InChI']
Isomeric_SMILES = GET['Isomeric_SMILES']
Core_level = GET['Core_level']
BE = GET['BE']
Reference_DOI = GET['Reference_DOI']

# Perform tasks using data

def load_pkl(category_filename):
	f = open(category_filename,"rb")
	category_list = pickle.load(f)
	f.close()
	return category_list

## This function parses a molecular formula string, and returns a dictionary with
## the elements present in the molecule as the keys, and the number of atoms of each
## element as values. A new element is assumed to start every time there is a
## capital letter.
##
## Data structures:
##
## MF_val = string
## MF_list = ["Symbol1numatoms1", "Symbol2numatoms2", ...], e.g. ["C2", "H6"]
## MF_dict = {element_1 : num_of_atoms_1 , element_2 : num_of_atoms_2 , ...}
def parse_molecular_formula(MF_val):
        MF_list = []
        symbol_and_num = ""
        if MF_val == "" or MF_val == None:
                return None
        else:
                for character in MF_val:
                        if character.isupper() == True:
                                if symbol_and_num != "":
                                        MF_list += [symbol_and_num]
                                symbol_and_num = character
                        else:
                                symbol_and_num += character
        if symbol_and_num != "":
                MF_list += [symbol_and_num]
        MF_dict = {}
        for symbol_and_num in MF_list:
                current_symbol = ""
                current_quantity = ""
                for character in symbol_and_num:
                        if character.isalpha() == True:
                                current_symbol += character
                        elif character.isnumeric() == True:
                                current_quantity += character
                if current_quantity != "":
                        current_quantity = int(current_quantity)
                else:
                        current_quantity = 1
                MF_dict[current_symbol] = current_quantity
        return MF_dict


def add_subscripts_to_CF_string(CF_val):
	string_with_subscripts = ""
	pre_previous_character = None
	previous_character = None
	for current_character in CF_val:
		if current_character.isdigit() and previous_character not in [" ","-","_",",","(",";",None]:
			if previous_character.isdigit() == False:
				string_with_subscripts += "<sub>"+current_character+"</sub>"
			elif previous_character.isdigit() and pre_previous_character not in [" ","-","_",",","(",";",None]:
				string_with_subscripts += "<sub>"+current_character+"</sub>"
			else:
				string_with_subscripts += current_character
		else:
			string_with_subscripts += current_character
		pre_previous_character = previous_character
		previous_character = current_character
	return string_with_subscripts


def get_entries_that_match_all_search_terms(GET):
	categories = ['MF','CF','IUPAC_Name','InChI','Isomeric_SMILES','Core_level','BE','Reference_DOI']
	sets_of_indices = []
	for category in categories:
		search_term = GET[category]
		if search_term.strip() != "":
			if category == "MF":
				search_term = parse_molecular_formula(search_term)
			if category == "BE":
				search_term = float(search_term)
			category_filename = "cgi-bin/"+category+"_list.pkl"
			category_list = load_pkl(category_filename)
			matching_indices = set()
			i = 0
			for entry in category_list:
				if category == "BE":
					if type(entry) == float:
						if abs(search_term - entry) < 0.001:
							matching_indices.add(i)
				elif category == "CF":
					if type(entry) == str:
						if (search_term == entry) or (search_term == entry.replace("*","")):
							matching_indices.add(i)
				elif category == "IUPAC_Name":
					if type(entry) == str:
						split_name = entry.split(",")
						for name in split_name:
							if search_term.casefold() == name.strip().casefold():
								matching_indices.add(i)
				elif search_term == entry:
					matching_indices.add(i)
				i += 1
			sets_of_indices += [matching_indices]
	entries_that_match_all_search_terms = set.intersection(*sets_of_indices)
	return entries_that_match_all_search_terms


def get_data_for_summary_table(set_of_entries):
	data_for_summary_table = {}
	for entry_number in set_of_entries:
		data_for_summary_table[entry_number] = {}
	for category in ['CF','Core_level','BE']:
		category_filename = "cgi-bin/"+category+"_list.pkl"
		category_list = load_pkl(category_filename)
		for entry_number in set_of_entries:
			value = category_list[entry_number]
#			if category == "CF":
#				value = add_subscripts_to_CF_string(value)
			data_for_summary_table[entry_number][category] = value
	return data_for_summary_table


entries_that_match_all_search_terms = get_entries_that_match_all_search_terms(GET)
data_for_summary_table = get_data_for_summary_table(entries_that_match_all_search_terms)
sorted_list_of_entry_numbers = sorted(list(entries_that_match_all_search_terms))

# Return data to print

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("<style>")
print("span {display : inline-block}")
print("sub {font-size : 75%}")
print("sup {font-size : 12.5%}")
print("</style>")
print("</head>")
print("<body>")
print("<p style='font-family: Courier New ; padding: 0px ; margin : 0px'> <span style='background-color : rgb(240,240,240) ; padding: 6px'> <b> Entry number &nbsp&nbsp&nbsp&nbspChemical Formula&nbsp&nbsp&nbsp&nbsp Core level&nbsp Binding Energy&nbsp </b> </span> </p>")
i = 0
for entry_number in sorted_list_of_entry_numbers:
	entry_number_string = str(entry_number).center(12).replace(" ","&nbsp;")
	CF_string = add_subscripts_to_CF_string(data_for_summary_table[entry_number]["CF"].center(24).replace(" ","&nbsp;"))
	subscript_count = CF_string.count("<sub>")
	CF_string_padding = "<sup>"
	for j in range(subscript_count):
		CF_string_padding += "&nbsp;"
	CF_string_padding += "</sup>"
	CF_string = CF_string_padding+CF_string+CF_string_padding
	Core_level_string = data_for_summary_table[entry_number]["Core_level"].center(12).replace(" ","&nbsp;")
	BE_string = str(data_for_summary_table[entry_number]["BE"]).center(16).replace(" ","&nbsp;")
	if (-1)**i == -1:
		print('''<p style='font-family: Courier New ; padding: 0px ; margin : 0px'> <span style='background-color : rgb(240,240,240) ; padding: 6px'> <a href='display_entry.py?entry_number=''' + str(entry_number) + "' style='text-decoration:none'>" + entry_number_string+"</a> "+CF_string+Core_level_string+BE_string+" </span> </p>")
	else:
		print('''<p style='font-family: Courier New ; padding: 0px ; margin : 0px'> <span style='background-color : rgb(255,255,255) ; padding: 6px'> <a href='display_entry.py?entry_number=''' + str(entry_number) + "' style='text-decoration:none'>" + entry_number_string+"</a> "+CF_string+Core_level_string+BE_string+" </span> </p>")
	i += 1
print("</body>")
print("</html>")

