def main():
    the_time = input("Enter current time: ")
    converted = convert(the_time)
    if  converted >= 7.0 and converted <= 8.0:
        print('Breakfast Time')
    elif converted >= 12.0 and converted <= 13.0:
        print('Lunch Time')
    elif converted >= 18.0 and converted <= 19.0:
        print('Dinner Time')
    else: 
        print('No food boss')


def convert(time):
    t = time.split(':')
    first_value = t[0] 
    second_value = str(float(t[1]) / 60).split('.')
    value = first_value +'.' + second_value[0] + second_value[1]
    return float(value)



if __name__ == "__main__":
    main()