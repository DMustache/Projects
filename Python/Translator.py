from googletrans import Translator

translator = Translator()

result = translator.translate('bottom' , src='en', dest='ru')

print(result.src)
print(result.dest)
print(result.text)