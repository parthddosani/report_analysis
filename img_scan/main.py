import pytesseract
from PIL import Image
import pandas as pd
import json
import csv
import itertools

img = Image.open('lab.png')
text = pytesseract.image_to_string(img,config='-c preserve_interword_spaces=1x1 --psm 4 --oem 3')
# df = pd.DataFrame(data=text)
# print(text)
reader = text.split('\n')
#print(reader)
j = 0
result = []

for i in reader:
    
    a= (i.split("  "))
    
    while '' in a:
        a.remove('')
    # b = a.split(' ')
    #a.remove("")
    #
    # a = filter(None,a)
    #b = [list(a[0]),list(a[1]),list(a[3])]
    #c = a[1]
    row = []
    if(len(a)>=3 and len(a)<=4) :
            row.append(a[0])
            row.append(a[1])
            if j ==0 :
                row.append(a[2])
            else :
                row.append(a[3])
            
            j=j+1
            # print(result)
    if(len(row) > 0):
        result.append(row)
        
#    # d = a[2]
#    # print(b)



# cols = ["A","B","C"]
# # df.to_excel(r'C:\Users\Harishankar\Desktop\spdsht.xlsx')
# # , delimiter=' '
# # reader = csv.reader(text.split('\n'))

lab_data = open('lab_data.csv', 'w')
csvwriter = csv.writer(lab_data)
for row in result:
    print('\t'.join(row))
       # col  = row.split(" ")
    csvwriter.writerow(row)
lab_data.close()
# # print(text[0:14])

#print(text)

