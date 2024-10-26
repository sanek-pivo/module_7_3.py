import string

class WordsFinder: # Напишем класс WordsFinder
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    var = string.punctuation
                    for p in string.punctuation:
                        if p in line:
                            line = line.replace(p, '')
                    words.extend(line.split())
            all_words[name] = words
        return all_words
    def find(self, word):
        position = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                position[key] = value.index(word.lower()) + 1
        return position
    def count(self, word):
        counter = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counter[value] = words_count
        return counter


print()
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
print()
finder3 = WordsFinder('test_3.txt')
print(finder3.get_all_words())  # Все слова
print(finder3.find('ouR'))  # 9 слово по счёту
print(finder3.find('sHiP'))  # 15 слово по счёту
print(finder3.count('capTain'))  # 4 слова capTain в тексте всего