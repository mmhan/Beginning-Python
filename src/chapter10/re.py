import re

def reTest():
    some_text = 'alpha, beta,,,,gamma    delta'
    print re.split('[, ]+', some_text)
    print re.split('[, ]+', some_text, maxsplit=2)
    print re.split('[, ]+', some_text, maxsplit=1)
    
    pat = '[a-zA-Z]+'
    text = '"Hm... Err --- are you sure?" he said, sounding insecure.'
    print re.findall(pat, text)
    pat = '[.?\-",]+'
    print re.findall(pat, text)
    
    pat = '{name}'
    text = "Dear {name}..."
    re.sub(pat, "Mr. Gumby", text)        
    
reTest()