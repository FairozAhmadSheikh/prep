listed=[1,2,3,4,5,6,7,8,9,10]

# list compre
lis2nd=["ODD" if value%2==1 else value for value in listed]
# print(lis2nd)
list3rd=[x if x %2==0 else " " for x in listed]
# print(list3rd)

# listh=["Sameer","esa","hussain"]

# add elements to ins
# listh.append("Feroz")
# listh+=["Rohullah"]
# listh[2]="malik"

# print(listh)

# print(listh.index("esa"))
# print("esa" in listh)

listo=[0,1,2,3,4,5,6,7,8,9]

# print(listo[1::2])

# listo += [10]
# print(listo)

# listo.insert(0,11)
# print(listo)

# listo.append(12)
# print(listo)

# # delete 
# listo.pop(0)
# print(listo)

# listo.remove(8)
# print(listo)

# del listo[0]
# print(listo)

# listo.clear()
# print(listo)

# listv=[9,8,7,6,3,2,1,5]
# listv.sort()
# print(listv)
# listdd=[1,2,3,4,5,6,7,8,9]
# listdd.sort(reverse=True)
# print(listdd)

# data in tuple cant change 

# coordinates=(True,"sameer","mohamed mutakeen malik",0.675,"sameer")
# print(coordinates)
# print(coordinates.count("sameer"))

# dictionaries : 

dict={
     "name":"Feroz",
     "Roll_no":652,
     "section":"a",
     }
    
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("section"))
print(dict["Roll_no"])

print("name" in dict)

# update 
dict["name"]="EESa"
dict["addr"]="Bandipora"
dict.update({"Roll_no":2})
dict.update({"aadhar":455642})

print(dict)
# remove 
dict.pop("addr")
print(dict)





