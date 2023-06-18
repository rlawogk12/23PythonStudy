phone_list1=["010-8248-3966","010-2052-9499","010-8258-3966"]
print(phone_list1)
phone_list2=[]
for number in phone_list1:
    x=number.replace("-","")
    phone_list2.append(x)
print(phone_list2)