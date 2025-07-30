tanxmovnebi = "bvdfghjklmnpqrstvwxyz"

while True:
    words = input("enter word: ").strip().lower()
    
    if len(words) < 2:
        print("the word must contain at least  2 letters. ")
        continue

    if words[0] in tanxmovnebi and words[-1] in tanxmovnebi :
        print("right. both the first and last letters are not vowel.")
        break
    else:
        print("first or last letter is a vowel.")