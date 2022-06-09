#access
a={1:"mango",2:"oreng",3:"apple"}
print(a)
print()

#add
a[4]="banana"
print(a)

#chang
a[2]="watermelan"
print(a)
print
#remove

a.pop(2)
print(a)
print()

#cheak

if "mango" in a[1]:
    print("mango is member is disc")
else:
    print("item not member this dics")

print()

for i in a.values():
    print(i)
