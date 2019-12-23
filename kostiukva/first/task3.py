"""
Програма, що рахує суму парних та не парних чисел
"""
odd_elements_sum = 0
even_elements_sum = 0
for elem in 'YOUR_LIST':
    if elem % 2 == 1 :
        odd_elements_sum+=elem
    else:
        even_elements_sum+=elem
print('even elements sum')