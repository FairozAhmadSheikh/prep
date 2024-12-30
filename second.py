d1={
    "name":"sameer",
    "roll_no":22,
    'age':23
}

print(d1)
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())

d1["age"]=22
print(d1)

d1.pop("name")
print(d1)



# sets
s1={1,2,3,4,5,6,7,8,9}
print(s1)

s1.add(10)
print(s1)

s1.add(11)
print(s1)

# for loop
for i in s1:
    print(i)


s1={1,2,3,4,5,6,6}
s2={6,7,8,9,10}
print(s1.union(s2))
print(len(s1))



sum=0
for i in range(1,8):
    sum+=i
    print(i,end="")
print()
print("sum is \n ",sum)



dictionar={
    "name":"ali"
}
dictionar.update({"roll_no":23})
print(dictionar)




"""
shopping program

"""





store={
    "laptops":{"price":199.2,"stock":23},
    "mobiles":{"price":293.8,"stock":33},
    "pendrive":{"price":169.7,"stock":35},
    "mouse":{"price":155.8,"stock":45},
    }
print("*****SHOPPING CART STARTS*****")
for k1,v1 in store.items():
    print(k1," : ", v1["price"],"$ ")
print("*****SHOPPING CART ENDS*******")

to_buy=input("What do you want to buy ? : ")

if to_buy in store:
    quantity=int(input("How Many You want : "))
    if quantity<=store[to_buy]["stock"]:
        bill=store[to_buy]["price"]*quantity
        print("Order placed Sucessfully ")
        print("Your Total $",bill)
    else:
        print("We dont have so many quantity ")
else:
    print("We dont have that item")