# coding:utf8
import re,os

a = "seg"
z = "seg_sym"

for _,_,j in os.walk(a):
    for i in j:
        with open(a+'/'+i, 'r',encoding='utf8') as fa:
            a_content=fa.read()
        all_NE = re.findall(r'(\[".*?", ".", "[BME]"\], )*', a_content)
        print(i,len(all_NE))
