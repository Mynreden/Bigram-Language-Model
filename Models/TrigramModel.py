import random
import pandas
import matplotlib.pyplot as plt
from Models.LanguageMidel import LanguageModel
from Models.BigramModel import read_data

MIN_LENGTH: int = 3
MAX_LENGHT: int = 8
ALPHABET: str = 'abcdefghijklmnopqrstuvwxyz'
URL: str = 'names.txt'


class TrigramLanguageModel(LanguageModel):
    def __init__(self):
        super(TrigramLanguageModel, self).__init__()

    def update(self, name: str) -> None:
        trigrams = self.get_trigrams(name)
        self.char_number += len(name) - 2

        for trigram in trigrams:
            if trigram in self.count:
                self.count[trigram] += 1
            else:
                self.count[trigram] = 1

            if trigram[0] in self.context:
                self.context[trigram[0]].append(trigram[1])
            else:
                self.context[trigram[0]] = [trigram[1]]

    def get_trigrams(self, word: str) -> list:
        length = len(word)
        trigrams = []
        for i in range(length - 2):
            trigrams.append(((word[i], word[i + 1]), word[i + 2]))
        return trigrams

    def get_next(self, context: tuple) -> str:
        try:
            variants = self.context[context]
            return random.choice(variants)
        except KeyError:
            return random.choice(ALPHABET)

    def generate(self) -> str:
        word = ''
        next = random.choice(ALPHABET)
        tuple1 = ('^', next)
        previous = ''
        while next != '$' or len(word) < MIN_LENGTH:
            if next == '$':
                next = self.get_next((previous, tuple1[0]))
                continue
            word += next
            previous = tuple1[0]
            next = self.get_next(tuple1)
            tuple1 = (tuple1[1], next)
            if len(word) == MAX_LENGHT:
                next = '$'
        return word


def create_trigram_model(data: list) -> TrigramLanguageModel:
    model = TrigramLanguageModel()
    for name in data:
        model.update(name)
    return model


def main() -> None:
    data = read_data(URL)
    model = create_trigram_model(data)
    random.seed(7)
    print('Generating 10 names:')
    for i in range(10):
        name = model.generate()
        print(name)


if __name__ == '__main__':
    main()
