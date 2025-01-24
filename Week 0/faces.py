def main():
    sen = input("")
    output = convert(sen)
    print(output)


def convert(sentence):
    sentence = sentence.replace(':)', '😊')
    sentence = sentence.replace(':(', '☹️')
    return sentence

main()




        
        