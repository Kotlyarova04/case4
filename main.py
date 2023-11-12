"""
Kotlyarova Polina 60
Rafaevich Vita 45
"""

import random

with open('input.txt', 'r', encoding='utf-8') as inp:
    sentences = int(inp.readline())
    text = inp.read()
    text = text.split()

word_dict = {}
previous = text[0]
for word in range(len(text)-1):
    current = text[word+1]
    if previous in word_dict:
        word_dict[previous].append(current)
    else:
        word_dict[previous] = [current]
    previous = current

bred = []
for i in range(sentences):
    sentence = []
    current_word = random.choice([word for word in word_dict if word[0].isupper()])
    sentence.append(current_word)
    while len(sentence) < 30:
        next_word = random.choice(word_dict[current_word])
        sentence.append(next_word)
        if next_word[-1] in '.!?':
            break
        current_word = next_word
    sentence = ' '.join(sentence)
    bred.append(sentence)

with open('output.txt', 'w', encoding='utf-8') as f_out:
    for sentence in bred:
        print(sentence, file=f_out)
