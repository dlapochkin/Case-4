from textblob import TextBlob

text = input()
syllables = 0
sentence = 0

for b in ['.', '!', '?']:
    if text.count(b) > 0:
        sentence += text.count(b)
print('Предложений:', sentence)

print('Слов:', text.count(' ') + 1)

if ord(text[0]) < 122:
    syllables = sum(1 for x in text.lower() if x in 'aeiou')
else:
    syllables = sum(1 for x in text.lower() if x in 'уеоаыяиюэ')
print('Слогов:', syllables)
print('Средняя длина предложения в словах:', (text.count(' ') + 1) / sentence)
print('Средняя длина слова в слогах:', syllables / (text.count(' ') + 1))

blob = TextBlob(text)
if blob.detect_language() == 'ru':
    blob = blob.translate(to="en")
if blob.sentiment.polarity > 0.33:
    tonality = 'Положительная'
elif blob.sentiment.polarity < -0.33:
    tonality = 'Отрицательная'
else:
    tonality = 'Нейтральная'
print('Тональность текста:', tonality)
obj = format(1 - blob.sentiment.subjectivity, '.1%')
print('Объективность:', obj)
