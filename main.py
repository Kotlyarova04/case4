with open('input.txt', 'r', encoding='utf-8') as inp:
    text = inp.read()
    text = text.split()
word_dict = {}
for word in text:
    if word not in word_dict:
        word_dict[word] = 1
    unique = []
    for words in text[text.index(word)+1:]:
        if words != word:
            if words not in unique:
                unique.append(words)
    word_dict[word] = unique


print(word_dict)
