def run_length_encoding(string):

    string = string.upper()
    prev_letter = string[0]
    prev_letter_count = 0
    output = ""

    for current_letter in string:
        if current_letter == prev_letter:
            prev_letter_count += 1

        else:
            output = output + str(prev_letter_count) + prev_letter
            prev_letter = current_letter
            prev_letter_count = 1

    output = output + str(prev_letter_count) + prev_letter

    return output


if __name__ == "__main__":
    string = input("Enter the string: ")
    output = run_length_encoding(string)
    print(output)