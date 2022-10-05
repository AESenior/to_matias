import re
import docx
import os,sys

ips='IPs.docx'
deliverable='IPsList.txt'

#donde tienes los IPs
doc=docx.Document(ips)

#donde pondras los IPs
save=open(deliverable,'w')

for i in doc.paragraphs:
    #para limpiar num porque si no se queda con el ultimo que leyo.
    num=''

    #Regex para separar las IP
    x = re.sub('\s+','/',i.text)
    x = re.split("[/,\t]", i.text, 1)

    ip=x[0]

    #Valida si tiene otra columna aparte del IP.
    #Para evitar que si viene el entry solo con IP no se rompa.
    if len(x)>1:
        num=re.split(",",x[1])

        for n in num:
            print(ip+"/"+n)
            
    else:
        print(ip)

#Guarda lo impreso en un .txt
sys.stdout = save

