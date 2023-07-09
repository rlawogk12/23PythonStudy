
temp={"월":15.5,"화":17.0,"수":16.2,"목":12.9,"금":11.0,"토":10.5,"일":13.3}
small_temp="토"
smallest=temp["토"]


for key in temp:
    if temp[key]>smallest:
        small_temp=key
        smallest=temp[key]
print("요일:%s" %small_temp)
print("최고기온:%d도" %smallest)





























