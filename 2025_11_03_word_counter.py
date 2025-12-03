def count_words(sentence):
    count = 1
    for i in sentence:
        if i == " ":
            count += 1
    return count


test = count_words("The quick brown fox jumps over the lazy dog.")
print(test)
