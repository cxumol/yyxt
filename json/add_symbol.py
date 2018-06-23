# coding:utf8
import re,os

a = "seg"
z = "seg_sym"

for _,_,files in os.walk(a):
    for afile in files:
        with open(a+'/'+afile, 'r',encoding='utf8') as fa:
            a_content=fa.read()
        all_NE = re.findall('''(?:\["[^"]+?", ".{1,4}", "[BME]"\], )+''', a_content)
        print(afile)
        all_NE=sorted(list(set(all_NE)))
#         for x in all_NE:
#             print(x)
            
        # 开始替换
#         print("替换为: ")
        ctrlfh= dict()
        for each in all_NE:
            ONE=re.sub('[BME]','.', each)
            ONE=re.sub('\[','\[', ONE)
            ONE=re.sub('\]','\]', ONE)
            ctrlfh[ONE]=each
#             print(ONE,':',ctrlfh[ONE])
        
        with open(z+'/seg_sym_'+afile[4:], 'w+',encoding='utf8') as fz:
            z_content=fz.read()
        
            z_new_content=z_content
            for k,v in ctrlfh.items():
                z_new_content=re.sub(k,v, z_new_content)
        
#             z_new_content=re.sub("", z_new_content)
            fz.write(z_new_content)
#         with open(z+'/'+'_BME'+i, 'w',encoding='utf8') as fb:
#             fb.write(z_new_content)