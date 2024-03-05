# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
i = 0
list_chars = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
i = sum([1 for char in list_chars for symbol in word.lower() if char == symbol])
print(i)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
print(*['\r' +word[0] + '\n' for word in sentence.split()])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
print(sum([len(word) for word in sentence.split()]) / len(sentence.split()))
