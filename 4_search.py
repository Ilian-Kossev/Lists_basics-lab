n = int(input())
word = input()
my_list = []
for _ in range(n):
    new_string = input()
    my_list.append(new_string)
print(my_list)
new_list = []
for element in my_list:
    if word in element:
        new_list.append(element)
print(new_list)