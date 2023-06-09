#!/usr/bin/python3

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

def load_pkl(category_filename):
        f = open(category_filename,"rb")
        category_list = pickle.load(f)
        f.close()
        return category_list

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


categories = ["MF",
		"CF",
		"IUPAC_Name",
		"Isomeric_SMILES",
		"InChI",
		"Core_level",
		"BE",
		"BE_comment",
		"Reference_DOI",
		"Reference_text",
		"Reference_comment",
		"Comment"]

category_display_names = {"MF" : "Molecular formula",
                "CF" : "Chemical formula",
                "IUPAC_Name" : "IUPAC name",
                "Isomeric_SMILES" : "SMILES identifier",
                "InChI" : "InChI identifier",
                "Core_level" : "Core level",
                "BE" : "Binding energy (eV)",
                "BE_comment" : "Binding energy comment",
                "Reference_DOI" : "Reference DOI",
                "Reference_text" : "Reference (text)",
                "Reference_comment" : "Reference comment",
                "Comment" : "Comment"}

entry_number = int(GET['entry_number'])
all_values = {}
for category in categories:
	category_filename = "cgi-bin/"+category+"_list.pkl"
	category_list = load_pkl(category_filename)
	category_value = category_list[entry_number]
	if category == "CF":
		category_value = add_subscripts_to_CF_string(category_value)
	all_values[category] = category_value

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h3 style='font-family: Courier New ; padding: 0px ; margin : 0px'> Database entry number "+str(entry_number)+"</h3>")
print("<hr>")
for category in categories:
	if all_values[category] != None:
		print("<p style='font-family: Courier New'> <b>"+category_display_names[category].rjust(19).replace(" ","&nbsp;")+":</b> "+str(all_values[category])+" </p>")
print("</body>")
print("</html>")

