def main():
    word = input("")
    snake_case = convert(word)
    print(snake_case)


def convert(word):
    for letter in word:
        if letter.isupper() == True:
            snake_case = word.replace(letter, '_' + letter.lower())
            return snake_case
    

main()
    





