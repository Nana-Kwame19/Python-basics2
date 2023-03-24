#last_name = "Nyanteh"
#phone_number = 233505857228
#age = 20

#print( first_name + last_name)
#print(phone_number)
#print (age)


#li_st=["Kelvin","Angel","Abena"]
#print(li_st)

# names_of_students = ["a","b","c"]
# print(names_of_students[1])
# names_of_students.append("d")
# print(names_of_students)

list_of_students = ["Kelvin","Angel","Abena","Michael","Donald"]
print(list_of_students)
list_of_students.append("David") #adding an item to a list
print(list_of_students)
print(list_of_students[2])
list_of_students.remove("Michael")# removing an item from a list
print(list_of_students)


#Dictionary format name={"keyname":"value"}
Kelvin_info = {"name":"Kelvin","age":19,"gender":"male"}
print(Kelvin_info)
print(Kelvin_info["age"])
myNew_info  = {"name":"Kelvin","age":19,"gender":"male",
               "hobbies": {"outdoor":["bastekball","football"],#A dictionary within a dictionary
                           "indoor":["sleeping","more sleep"]}
               }
print(myNew_info)
print(myNew_info["hobbies"])

hobbies = myNew_info["hobbies"]
print(f"My hobbies are {hobbies}")

outdoor = hobbies["outdoor"]
print(f"My outdoor hobbies are {outdoor}")





print("Enter your name:")
x = input()
print("Hello, " + x)