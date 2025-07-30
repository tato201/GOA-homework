# #1)
xmovnebi = "aeiou"

while True:
    words = input("enter word: ").strip().lower()
    
    if len(words) < 2:
        print("the word must contain at least  2 letters. ")
        continue

    if words[0] not in xmovnebi and words[-1] not in xmovnebi :
        print("right. both the first and last letters are not vowel.")
        break
    else:
        print("only first or last letter is a vowel.")
# 2)

correct_words = []
for i in range(5):
    word = input(f"word {i+1}: ")
    if word[0] not in xmovnebi and word[-1] not in xmovnebi:
        correct_words.append(word)

print(correct_words)

#3)
count = 0
for i in range(5):
    word = input(f"word {i+1}: ")
    if len(word) >= 2 and word[0] not in xmovnebi and word[-1] not in xmovnebi:
        count += 1
print(count)



for i in range(10):
    word = input(f"word {i+1}: ")
    if len(word) >= 2 and word[0] not in xmovnebi and word[-1] not in xmovnebi:
        print(word)


# 4)
vowel = 0
conant = 0
word = input("please enter your word: ")
while word[0] not in xmovnebi and word[-1] not in xmovnebi:
    for i in word:
        if i in xmovnebi:
            vowel += 1
        else:
            conant += 1
    print(vowel)
    print(conant)
    sityva1 = input("anything ")
    if word[0] not in xmovnebi and word[-1] not in xmovnebi:
        print("correct")
else:
    print("incorerct1")
#5)
while True:
    word = input("a ")
    vowel = 0
    consonant = 0
    for i in word:
        if i in xmovnebi:
            vowel += 1
        else:
            consonant += 1
    print(vowel)
    print(consonant)
    if len(word) >= 2 and word[0] not in xmovnebi and word[-1] not in xmovnebi:
        print("correct")
        break
    else:
        print("incorrect")
    
        

