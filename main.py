from textblob import TextBlob
text = input()
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