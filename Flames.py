# input names in string which will be converted in to list using list() function
name1 = list(input("enter the name1 :"))
name2 = list(input("enter the name2 :"))

#  converting the name list in to string for the end statement or output
n1=""
n2=""
for nn in name1:
    n1 +=nn
for mm in name2:
    n2 +=mm

# Removing the common letters from the names
for i in name1:
    if i in name2:
        name1.remove(i)
        name2.remove(i)

# length of both names combined to count the non matching letters from both names
common = (len(name1)+len(name2))

# Removing the letter from the flames string everytime the loop matches the count
flames =list("flames")
index = 0
ele = ""
while len(flames) > 1 :
    for a in flames:
        index +=1
        ele = a
        if index == common:
            index = 0
            flames.remove(ele)
            # print(flames)

# creating a dictionary for the meaning of each letter in flames 
dict = {"f":"friends", "l":"lovers","a":"affection","m":"marriage","e":"enemys","s":"siblings"}

# Printing the output
print(f"{n1} & {n2} will be {dict[flames[0]]}")
# print(dict[flames[0]]) -- if we want only the relation

