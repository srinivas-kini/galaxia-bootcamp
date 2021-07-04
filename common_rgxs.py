import re

phone_nmbrs = '''
             111-222-3333  
             444.555.6666
             +91 9820774218
             +91 9830083685
             +91 9833082685
             400703
             500705
             '''

emails = '''
kinisrinivas96@gmail.com
abc@gmail.com
abc@xy_z.org
someemail@.com
'''

xml_tags = '''
<xml> </xml>
'''

us_phn_matcher = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}').finditer(phone_nmbrs)
ind_phn_matcher = re.compile(r'\+91\s\d{10}').finditer(phone_nmbrs)
ind_zipcode_matcher = re.compile(r'\b\d{6}\b').finditer(phone_nmbrs)
email_matcher = re.compile(r'[a-z0-9_.-]+@[a-z0-9_.-]+\.\w{3}').finditer(emails)
xml_tag_matcher = re.compile(r'</?[a-zA-Z0-9]+>').finditer(xml_tags)


