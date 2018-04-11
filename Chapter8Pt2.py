def remove_letter(letter, word):
    new = ""
    for ch in word:
        if ch != letter:
            new += ch
    return new

remove_letter("a", "Bus")

def remove(phrase, word):
    new = word.replace(phrase, "")
    return new


print(remove("yes", "no"))

def count_a(text, letter):
    count = 0
    for c in text:
        if c == letter:
            count += 1
    return(count)
print(count_a("Car", "x"))
