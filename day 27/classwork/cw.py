# 1
word = input("შეიყვანე სიტყვა: ")

if len(word) > 5:
    print("პატარა ასოებით:", word.lower())
else:
    print("დიდი ასოებით:", word.upper())

# 2
def find_first_letter_position(text, letter):
    position = text.find(letter)
    if position == -1:
        return "ასო ვერ მოიძებნა"
    return f"პირველად {letter} მდებარეობს ინდექსზე: {position}"
    
# 3
def create_welcome_message(name):
    return f"მოგესალმები, {name}. წარმატებები!"



