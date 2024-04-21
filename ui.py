import note


def create_note(number):
    title = check_len_text_input(
        input("Input note title: "), number)
    body = check_len_text_input(
        input("Input note body: "), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\n1 - reading all notes from a file\n"
          "2 - add note\n"
          "3 - delete note\n"
          "4 - edit note\n"
          "5 - selecting notes by date\n"
          "6 - find a note by id\n"
          "7 - exit\n\n"
          "Input number: ")


def check_len_content_input(text, n):
    while len(content) <= n:
        print(f"The content should be larger {n} characters\n")
        content = input("Input text: ")
    else:
        return text


def goodbuy():
    print("We are waiting for your return. Goodbuy!")
