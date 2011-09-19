# template.py

import fileinput, re

# matches fields enclosed in square brackes
field_pat = re.compile(r'\[(.+?)\]')

# We'll collect variablse in this:
scope = {}

# this is used in re.sub
def replacement(match):
    code = match.group(1)
    try:
        #if the field can be evaluated return it:
        return str(eval(code, scope))
    except SyntaxError:
        #otherwise execute the assignment in the same scope
        exec code in scope
        # ... and return an empty string:
        return ''
    
#get all the text as a single string:
lines = []
for line in fileinput.input():
    lines.append(line)
    
text = ''.join(lines)

# Substitute all the occurences of the field pattern:
print field_pat.sub(replacement, text)

# try this out by using python template.py template.tpl