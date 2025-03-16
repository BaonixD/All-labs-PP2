import re 


with open ( r"D:\PP2\labs\lab5\8-9-10.txt" ) as f:
    data = f.read()
matches=re.sub(r"[A-Z]",'_',data)
print(matches)