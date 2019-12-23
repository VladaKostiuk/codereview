"""
Програма, що рзнаходить слова, що починаються з великої літери
"""

user_text = input('enter text')
capitalize_list = []
for word in user_text.split(''):
    if word != word.lower():
        capitalize_list.append(word)

print(capitalize_list)