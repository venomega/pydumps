fd = open("file.txt", "br")
tag=["<p>Confirmados"]   #, "<p>Ingresados", "<p>Recuperados","<p>Fallecidos" ] 
db = ["Confirmados", "Ingresados","Recuperados","Fallecidos"]
lines= [1344,1348,1352,1356]
line_count = 0
another_count=0

result=[]

def get_lines(fd,tag):
    lines=0
    for i in fd:
        lines += 1
        if tag[0].encode() in i:
            return [lines + 1, lines+5,lines+9,lines+13]

tag = get_lines(fd,tag)

fd.close()
fd = open("file.txt", "br")

line_count= 0
another_count= 0
for i in fd:
    line_count+=1
    if line_count == tag[another_count]:
        result.append(i)
        another_count+=1
        if another_count > 3:
            break



for i in range(len(result)):
    print (db[i], result[i].decode()[37:-11])


