def main():
    greet = input(str("Hi!"))
    output = convert(greet)
    print(output)


def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")


main()
