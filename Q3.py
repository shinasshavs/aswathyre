# list1=[]
# a=[]
# n1 = int(input("Enter the number of elements: "))
# for i in range(n1):
#       elements = str(input("Enter element"+str(i)+":"))
#       list1.append(elements)
# print(list1)

# a = []
# list1 = input("Enter the elements separated by space: ").split()
# print("The entered elements are:", list1)
# for x in list1:
#          if int(x)<10:
#              a.append(x)
# print("The numbers below 10 is:",end=" ")
# for i in a:
#     print(i,end=",")
# # Get input strings from the user
# string_inputs = []
# num_inputs = int(input("How many strings do you want to input? "))
# for i in range(num_inputs):
#     string_inputs.append(input(f"Enter string {i+1}: "))
#     print(string_inputs)
#
# # Combine the strings with commas
# result = ""
# for i in range(len(string_inputs)):
#     result += string_inputs[i]
#     if i < len(string_inputs) - 1:
#         result += ","
#
# # Print the result
# print(result)
#





# x=str(input("enter string:")).split()
# for i in x:
#      print(str(x),end=",")

#
# list1=[]
# a=[]
# n1 =int(input("Enter the number of elements: "))
# for i in range(n1):
#       elements = int(input("Enter element"+str(i)+":"))
#       list1.append(elements)


# list1=[]
# a=[]
# n1 = int(input("Enter the number of elements: "))
# for i in range(n1):
#       list1.append(input(f"Enter string {i+1}: "))
# for i in list1:
#        print(i,end
#          print(a[i],end=",")
# words = 'Hello', 'world', 'how', 'are', 'you'
# s1 = ','.join()
# print()

#
#
# num_list = []
#
# n = int(input("Enter the number of integers in the list: "))
#
# for i in range(n):
#     num = int(input("Enter an integer: "))
#     num_list.append(num)
#
# print("The list of integers is:", num_list)

#
# num_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
#
# print("The list of integers is:", num_list)
# a = int(input("Enter the elements separated by space: ").split())
# print("The entered elements are:",int(a))



# num_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
# target_num = int(input("Enter the target integer: "))
#
# closest_num = num_list[0]
# closest_diff = closest_num - target_num
#
# for num in num_list:
#     diff = num - target_num
#     if diff < 0:
#         diff = -diff
#     if diff < closest_diff:
#         closest_num = num
#         closest_diff = diff
#
# print("The closest number to", target_num, "is", closest_num)

#
# num_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
# target_num = int(input("Enter the target integer: "))

closest_num = num_list[0]

for num in num_list:
    if abs(num - target_num) < abs(closest_num - target_num):
        closest_num = num

print("The closest number to", target_num, "is", closest_num)

