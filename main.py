text = input()
syllables=0
sentence=0
asl=0

for b in['.','!','?']:
    if text.count(b)>0:
        sentence += text.count(b)
print('Предложений:', sentence)

import re
word = len(re.findall(r'\w+', text))
print('Слов:', word)

if ord(text[0])<122:
    syllables=sum(1 for x in text if x in 'aeiou')
else:
    syllables = sum(1 for x in text if x in 'уеоаыяиюэ')
print('Слогов:',syllables)

words = re.split('\w', text)
asl = sum(len(word) for word in words) / len(words)
print('Средняя длина слова в слогах:', asl, words)







