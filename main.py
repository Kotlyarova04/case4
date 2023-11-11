with open('input.txt', 'r', encoding='utf-8') as inp:
    text = inp.read()
    text = text.split()
word_dict = {}
for word in range(len(text)):
    if text[word] not in word_dict:
        word_dict[text[word]] = 1
print(word_dict)
