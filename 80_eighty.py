import snake


def main():
    one_dict = {'1':'one', '2':'two', '3':'three', '0':'zero',
                '4':'four', '5':'five', '6':'six',
                '7':'seven', '8':'eight', '9':'nine'}

    two_dict = {'10':'ten', '11':'eleven', '12':'twelve',
                '13':'thirdteen', '14':'fourteen', '15':'fifteen',
                '16':'sixteen', '17':'seventeen', '18':'eighteen',
                '19':'nineteen', '20':'twenty'}

    user_input = snake.i('Enter your number: ','num')
    count = len(user_input)


    s = ''
    spell = ''
    print(today)
    for i in user_input:
        if count in range(3,count,3):
            spell = 'Hundred'
        elif count in range(2,count,3):
            spell = two_dict.get(i)
        elif count == 1:
            spell = ''
        
        elif count == 4:
            spell = 'thousand'
        elif count == 7:
            spell = 'million'

        s = s + ' ' + one_dict[i] + spell
    print(s)


if __name__ == '__main__':
    main()
