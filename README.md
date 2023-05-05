# Tutorial
Run main.py file. It will generate 3 names using different language models: Bigram, Trigram, Ngram. You can also run scripts individually from the Models folder. Each script generates 10 names based on its own logic.

Graphs and table of propabity according to dataset is located in Graphs.ipynb. I used matplotlib and pandas libraries to generate graphs.

Example:
This graph shows what is the most likely letter to come after the letter "a".
![image](https://user-images.githubusercontent.com/110660562/236516187-7960e8fa-c92f-4205-a1b3-63309160e46f.png)


# Simple Language-Models
There you can see simple realization of Languge models based on statistic

. Bigram model - model that predict next character according to last character in given word

. Trigram model - model that predict next character according to last two characters in given word

. N-gram model - model that predict next character according to last (N - 1) characters in given word

# Abstract class Language Model 
Language Model class - is an abstract class that have abstract methods update(str), get_next(str), generate().


. update(str) method - add data from dataset to a class

. get_next(tuple) method - returns pridicted charachter according to previous characters

. generate() method - return fully generated name

. get_probability(tuple) - return dictionary where keys - possible predicted character according to context and values - propability of this character

. get_all_probabilities() - return dictionary where keys - previous context and values - list of tuples of possible predicted character and propability of this character. 
(Example {'a': [('e', 299), ('m', 2)})
# Bigram Language model
Bigram Language model - is an subclass of Language Model. Its predict next character according to last character in given word. It is not best variation of statistic based language model.

# Trigram Language model
Trigram Language model - is an subclass of Language Model. Its predict next character according to last two characters in given word. This model is more effective than Bigram Model

# N-gram Language model
 N-gram model is built by counting how often word sequences of N words occur in text and then estimating the probabilities and predict next character. It is more effective while generating long sequences from large dataset 
