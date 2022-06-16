import json
import csv

file_name = "GTM-NCPJSB_workspace1000463"
gtm_json = open("GTM-NCPJSB_workspace1000463.json")
gtm_python = json.load(gtm_json)
print(gtm_python)