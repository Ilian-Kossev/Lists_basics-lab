n = int(input())
number_list = []
filtered_list = []
for _ in range(n):
    number = int(input())
    number_list.append(number)
filter = input()
if filter == "even":
    for integer in number_list:
        if integer % 2 == 0:
            filtered_list.append(integer)
elif filter == "odd":
    for integer in number_list:
        if integer % 2 == 1:
            filtered_list.append(integer)
elif filter == "positive":
    for integer in number_list:
        if integer >= 0:
            filtered_list.append(integer)
elif filter == "negative":
    for integer in number_list:
        if integer < 0:
            filtered_list.append(integer)

print(filtered_list)