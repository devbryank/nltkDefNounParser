import nltk

# read text
with open('Firearms.txt', 'r') as file:
    content = file.read().replace('\n', '')

# lambda conditional (not used)
# is_noun = lambda pos: pos[:2] == 'NN'

# tokenize the content
tokens = nltk.word_tokenize(content)

# tag the content
tagged = nltk.pos_tag(tokens)

# extract target tagged word (not used)
# extracted = [word for (word, pos) in nltk.pos_tag(tokens) if is_noun(pos)]

# definite nouns
def_nouns = nltk.FreqDist(w2 for ((w1, t1), (w2, t2))
                          in nltk.bigrams(tagged)
                          if w1.lower() == "the" and t2 == "NN")

# get noun list
noun_list = []
for noun in def_nouns.keys():
    noun_list.append(noun)

# sort ascending order
noun_list.sort()

# print result
print(noun_list)
