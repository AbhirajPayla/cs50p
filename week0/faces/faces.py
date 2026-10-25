def main():
    value = input()
    new_value = convert(value)
    print(new_value)


def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji


main()
