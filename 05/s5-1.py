file_names=["file1.py","file2.txt","file3.pptx","file4.doc"]
for i in file_names:
    name, code = i.split('.')
    print("%s=>파일명:%s,확장자:%s" %(i,name,code))
