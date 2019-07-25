# s1 = "Arjuna"
# s2 = s1
# print(s1)
# print(s2)
#
# s3 = str(s1)
# print(s3)
#
# print(s1 == s2)
# print(s1 == s3)
#
# print(s1 is s2)
# print(s1 is s3)

list1 = [1, 2, 3, 4]
list2 = list1

list3 = list(list1)

print(list1 == list2)
print(list1 == list3)
print(list1 is list2)
print(list1 is list3)


"""
As u can see that for e.g.
if list1's address os 000
we are assigning list2 = list1, which means we are assigning list1's address to list2

so both list1 and list2 are pointing to same list i.e. they both have same address 000

now list3 = list(list1), this statement has created a new list object and assigned the address to list3

so == operator will compare the content of the two operands and will return true if the
content of two operands are equal where as 'is' operator will check whether the both operands are pointing
to same object or not, i.e. they should both have the address of the same object then it will return 
True else return False.

"""