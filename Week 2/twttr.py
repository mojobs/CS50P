text = input("")
for i in text.lower():
    if i== 'a' or i == 'i' or i == 'e' or i == 'u' or i == 'o':
        text = text.replace(i, '')
print(text)