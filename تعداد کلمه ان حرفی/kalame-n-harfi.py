# Taha Taghipour
# Sun. 7:45


count = 1
chrw = ""
   

file = open('textfile.txt', 'r')
while 1:
    sp = file.read(1)
   
    if count<= 3:
        chrw = chrw + sp
   
    if count>3:
        if sp ==" ":
            count = 0
            if len(chrw)>0:
                print(chrw)
                chrw =""
        elif sp !=" ":
            chrw =""
    count = count + 1
   
    if not sp:
        break
   
file.close()