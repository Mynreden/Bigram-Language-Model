import random
import pandas
import matplotlib.pyplot as plt

MIN_LENGTH: int = 3
ALPHABET: str = 'abcdefghijklmnopqrstuvwxyz'
URL: str = 'names.txt'

def read_data(url: str) -> list:
    names = []
    with open(url, 'r') as file:
        a = file.readline()
        while a:
            names.append('^' + a.replace('\n', '$'))
            a = file.readline()
    return names


class LanguageModel:
    def __init__(self):
        self.count: dict = {}
        self.context: dict = {}
        self.char_number = 0

    def update(self, name: str) -> None:
        bigrams = self.get_bigrams(name)
        self.char_number += len(name) - 2

        for bigram in bigrams:
            if bigram in self.count:
                self.count[bigram] += 1
            else:
                self.count[bigram] = 1

            if bigram[0] in self.context:
                self.context[bigram[0]].append(bigram[1])
            else:
                self.context[bigram[0]] = [bigram[1]]

    def get_bigrams(self, word: str) -> list:
        length = len(word)
        bigrams = []
        for i in range(length - 1):
            bigrams.append((word[i], word[i + 1]))
        return bigrams

    def get_next(self, context: str) -> str:
        variants = self.context[context]
        return random.choice(variants)

    def generate(self) -> str:
        word = ''
        next = self.get_next('^')
        previous = ''
        while next != '$' or len(word) < MIN_LENGTH:
            if next == '$':
                next = self.get_next(previous)
                continue
            word += next
            previous = next
            next = self.get_next(next)
        return word

    def get_probability(self, character: str) -> dict:
        variants = self.context[character]
        data = {}
        for char in variants:
            if char in data:
                data[char] += 1
            else:
                data[char] = 1
        data.pop('$')
        #for key, value in data.items():
        #    data[key] = round(value / self.char_number, 5)
        return data

    def get_all_probabilities(self) -> dict:
        result = {}
        for char in ALPHABET:
            data = self.get_probability(char)
            for i in ALPHABET:
                if i not in data:
                    data[i] = 0
            result[char] = sorted(list(data.items()), key=lambda x:x[0])
        return result


def create_language_model(data: list) -> LanguageModel:
    model = LanguageModel()
    for name in data:
        model.update(name)
    return model

def main() -> None:
    data = read_data(URL)
    model = create_language_model(data)
    random.seed(6)
    print('Generating 10 names:')
    for i in range(10):
        name = model.generate()
        print(name)

if __name__ == '__main__':
    main()
