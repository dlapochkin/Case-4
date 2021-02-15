text = input()
syllables=0
sentence=0

for b in['.','!','?']:
    if text.count(b)>0:
        sentence += text.count(b)
print('Предложений:', sentence)

print('Слов:',text.count(' ')+1 )

if ord(text[0])<122:
    syllables=sum(1 for x in text if x in 'aeiou')
else:
    syllables = sum(1 for x in text if x in 'уеоаыяиюэ')
print('Слогов:',syllables)








