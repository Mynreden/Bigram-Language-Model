class LanguageModel:
    def __init__(self):
        self.count: dict = {}
        self.context: dict = {}
        self.char_number = 0

    def update(self, name: str):
        pass

    def get_next(self, context: tuple) -> str:
        pass

    def generate(self) -> str:
        pass

    def get_probability(self, character: str) -> dict:
        variants = self.context[character]
        data = {}
        for char in variants:
            if char in data:
                data[char] += 1
            else:
                data[char] = 1
        print(data)
        # data.pop('$')
        # for key, value in data.items():
        #    data[key] = round(value / self.char_number, 5)
        return data

    def get_all_probabilities(self) -> dict:
        result = {}
        for char in ALPHABET:
            data = self.get_probability(char)
            for i in ALPHABET:
                if i not in data:
                    data[i] = 0
            result[char] = sorted(list(data.items()), key=lambda x: x[0])
        return result


def read_data(url: str) -> list:
    names = []
    with open(url, 'r') as file:
        a = file.readline()
        while a:
            names.append('^' + a.replace('\n', '$'))
            a = file.readline()
    return names

