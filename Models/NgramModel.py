import random
import pandas
import matplotlib.pyplot as plt
from Models.LanguageMidel import LanguageModel, read_data

MIN_LENGTH: int = 3
MAX_LENGHT: int = 8
ALPHABET: str = 'abcdefghijklmnopqrstuvwxyz'
URL: str = '../datasets/names.txt'


class NgramLanguageModel(LanguageModel):
    def __init__(self, n):
        self.n = n
        super(NgramLanguageModel, self).__init__()

    def update(self, name: str) -> None:
        ngrams = self.get_ngrams(name)
        self.char_number += len(name) - 2

        for ngram in ngrams:
            if ngram in self.count:
                self.count[ngram] += 1
            else:
                self.count[ngram] = 1

            if ngram[0] in self.context:
                self.context[ngram[0]].append(ngram[1])
            else:
                self.context[ngram[0]] = [ngram[1]]

    def get_ngrams(self, word: str) -> list:
        length = len(word)
        ngrams = []
        for i in range(length - self.n + 1):
            ngrams.append((tuple(word[i + j] for j in range(self.n - 1)), word[i + self.n - 1]))
        return ngrams

    def get_next(self, context: tuple) -> str:
        try:
            variants = self.context[context]
            if len(set(variants)) == 1 and variants[0] == '$':
                return random.choice(ALPHABET)
            return random.choice(variants)
        except KeyError:
            return random.choice(ALPHABET)

    def generate(self) -> str:
        word = ''
        next = random.choice(ALPHABET)
        previous = ''
        tuple1 = ('^', next) + tuple(random.choice(ALPHABET) for _ in range(self.n - 3))

        while next != '$' or len(word) < MIN_LENGTH:
            if next == '$':
                next = self.get_next((previous,) + tuple(tuple1[i] for i in range(self.n - 2)))
                continue
            word += next
            next = self.get_next(tuple1)
            previous = tuple1[0]
            tuple1 = tuple(tuple1[i] for i in range(1, self.n - 1)) + (next,)
            if len(word) == MAX_LENGHT:
                next = '$'
        return word


def create_ngram_model(data: list, n: int) -> NgramLanguageModel:
    model = NgramLanguageModel(n)
    for name in data:
        model.update(name)
    return model


def main() -> None:
    data = read_data(URL)
    model = create_ngram_model(data, 4)
    random.seed(7)
    print('Generating 10 names:')
    for i in range(10):
        name = model.generate()
        print(name)


if __name__ == '__main__':
    main()
