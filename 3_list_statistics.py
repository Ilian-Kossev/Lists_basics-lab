n = int(input())
list_positives = []
list_negatives = []

for i in range(n):
    num = int(input())
    if num >= 0:
        list_positives.append(num)
    else:
        list_negatives.append(num)
print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}. Sum of negatives: {sum(list_negatives)}")
