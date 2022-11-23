######sets#########3
my_set={1,2,3,4,5,6,7,8,9,10,10}
print(my_set)
print(len(my_set))

my_set.add("Diego Cuellar")
print("Diego Cuellar" in my_set)
print(10 in my_set)
print(my_set)
if "Diego Cuellar" in my_set:
    my_set.remove("Diego Cuellar")
else:
    print("Diego cuellar, no se encuentra en el set")
print(my_set)

my_other_set={1,2,3,4,"python","java","php"}
print(my_set)
print(my_other_set)

my_new_set = my_set.union(my_other_set).union("C","C++","C#")

print(my_new_set)
print(my_new_set.difference(my_set))

my_other_set_1={"C","C++","C#"}
print(my_other_set_1)

my_dic=dict()
