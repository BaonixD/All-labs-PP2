import re 


<<<<<<< HEAD:labs/lab5/10.py
with open ( r"D:\PP2\labs\lab5\8-9-10.txt" ) as f:
    data = f.read()
=======
with open(r"D:\PP2\labs\lab5\8-9-10.txt", encoding="utf-8") as f: #Заменяет каждую заглавную букву '_'
    data = f.read()

>>>>>>> 6b0daea7c69d8f6dd74f7293727203d33daf29d6:lab5/10.py
matches=re.sub(r"[A-Z]",'_',data)
print(matches)