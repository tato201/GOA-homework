
def sentence_to_comma_list(sentence):
    words = sentence.split()
    return ", ".join(words)
print(sentence_to_comma_list("ეს არის მაგალითი წინადადება"))

def print_word_lengths(sentence):
    words = sentence.split()
    for word in words:
        print(f"'{word}' - {len(word)} სიმბოლო")
print_word_lengths("ეს არის ტესტი ფუნქციისთვის")

def remove_extra_spaces(sentence):
    cleaned = " ".join(sentence.split())
    return cleaned
print(remove_extra_spaces("ეს   არის    წინადადება   ზედმეტი   სპეისებით"))


def spaces_to_dashes(sentence):
    words = sentence.split()
    return "-".join(words)
print(spaces_to_dashes("ეს არის ტესტი"))

def reverse_word_order(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
print(reverse_word_order("ეს არის შებრუნებული წინადადება"))
