def main():
    message()

def message():
    age = 17
    if (age >= 18):
        print('You are of age and you can go the club, your age is'.format(age)) 
    else:
        print(f'You can\'t go to the club because your age is. {age}')
    

if __name__ == '__main__': main()