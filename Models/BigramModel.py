import random
import pandas
import matplotlib.pyplot as plt
from Models.LanguageMidel import LanguageModel
MIN_LENGTH: int = 3
MAX_LENGHT: int = 8
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


class BigramLanguageModel(LanguageModel):
    def __init__(self):
        super(BigramLanguageModel, self).__init__()

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
        try:
            variants = self.context[context]
            return random.choice(variants)
        except KeyError:
            return random.choice(list(self.context.keys()))

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
            if len(word) == MAX_LENGHT:
                next = '$'
        return word


def create_bigram_model(data: list) -> BigramLanguageModel:
    model = BigramLanguageModel()
    for name in data:
        model.update(name)
    return model


def main() -> None:
    data = read_data(URL)
    model = create_bigram_model(data)
    print('Generating 10 names:')
    for i in range(10):
        name = model.generate()
        print(name)


if __name__ == '__main__':
    main()
