def main():
    #write your code below this line
    while True:
        phrase = input()

        if phrase == '':
            break

        words = phrase.split()

        for word in words:
            print(word)

if __name__ == '__main__':
    main()
