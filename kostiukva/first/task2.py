"""
Програма, що знаходить кількість пустих списків
"""
empty_list_count = 0
for elem in 'YOUR_LIST':
    if (elem == []):
        empty_list_count+=1
print(empty_list_count)