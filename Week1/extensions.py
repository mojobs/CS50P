file_name = input("File name: ")
if file_name.endswith('.gif'):
    print(f'image/gif')
elif file_name.endswith('.jpg'):
    print(f'image/jpeg')
elif file_name.endswith('.jpeg'):
    print(f'image/jpeg')
elif file_name.endswith('.png'):
    print(f'image/png')
elif file_name.endswith('.pdf'):
    print(f'application/pdf')
elif file_name.endswith('.txt'):
    print(f'image/txt')
elif file_name.endswith('.zip'):
    print(f'image/zip')
else:
    print('application/octet-stream')