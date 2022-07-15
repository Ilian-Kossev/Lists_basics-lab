n = int(input())
number_list = []
filtered_list = []
for _ in range(n):
    number = int(input())
    number_list.append(number)
filter = input()
for integer in number_list:
    if filter == "even":
        if integer % 2 == 0:
            filtered_list.append(integer)
    elif filter == "odd":
        if integer % 2 == 1:
            filtered_list.append(integer)
    elif filter == "positive":
        if integer >= 0:
            filtered_list.append(integer)
    elif filter == "negative":
        if integer < 0:
            filtered_list.append(integer)

print(filtered_list)