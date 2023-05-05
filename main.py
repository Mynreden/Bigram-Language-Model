from Models.BigramModel import read_data, BigramLanguageModel, create_bigram_model
from Models.TrigramModel import TrigramLanguageModel, create_trigram_model
from Models.NgramModel import NgramLanguageModel, create_ngram_model

URL: str = 'datasets/names.txt'


def main():
    data = read_data(URL)
    bigram = create_bigram_model(data)
    trigram = create_trigram_model(data)
    ngram = create_ngram_model(data, 4)

    for i in (bigram, trigram, ngram):
        print(i.generate())


if __name__ == '__main__':
    main()
