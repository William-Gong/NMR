#Read T1, T2, SD, chemical shift range from bruker generated file
#Fixed problem with reading intensity fitting
import re

txt = open('/Users/williamgong/Desktop/T1.txt') #open bruker generated file
txt_read = txt.read()


number1 = re.compile(r'-(\d*\.\d*)|(\d*\.\d*)') #get CS range
number2 = re.compile(r'(\d*\.\d*)m|(\d*\.\d*)s') #get t1 or t2
number3 = re.compile(r'\d*\.\d*e-\d*') #get standard deviation


mode1 = re.compile(r'-\d*\.\d* to .* ppm|\d*\.\d* to .* ppm|Point.*at.*ppm')
range_list = []
rag = mode1.findall(txt_read)
for n in rag:
    for nm in number1.finditer(n):
        range_list.append(nm.group())
        
if re.match(r'Point', rag[0]): #read as intensity fitting
    print "Peak Point:"
    for n in range(len(range_list)):
        print range_list[n], "ppm"
else: #read as area fitting
    print "Chemical shift range:"
    for n in range(len(range_list)-1):
        if n % 2 == 0:
            print range_list[n], "to", range_list[n+1], "ppm"
            
            
mode2 = re.compile(r'T1.*')
T1 = mode2.findall(txt_read)
print "T1/T2 value:"
for n in T1:
    for nm in number2.finditer(n):
        print nm.group()

        
mode3 = re.compile(r'SD.*')
SD = mode3.findall(txt_read)
print "Standard deviation value:"
for n in SD:
    for nm in number3.finditer(n):
        print nm.group()
