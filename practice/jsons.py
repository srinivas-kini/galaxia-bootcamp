import json

srinivas_kini_str = '''  
{
"first_name": "Srinivas",
"last_name": "Kini",
"age":25,
"height_cm": 174,
"weight_kg": 70,
"address": {
"street": "Jayshankar CHS, Plot 78",
"sector": "29",
"city": "Navi Mumbai",
"state": "Maharashtra",
"country": "India"
}
}
'''
# JSON String

srinivas_kini_dict = json.loads(srinivas_kini_str)  # loads -> load string : Converts a JSON string to a dict.
srinivas_kini_str_formatted = json.dumps(srinivas_kini_dict,
                                         indent=2)  # dumps -> dump string : Converts a python dict to str.
print(srinivas_kini_str_formatted)
