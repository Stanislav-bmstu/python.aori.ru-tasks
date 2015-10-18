# coding=utf-8

__author__ = 'stanislav.bmstu'


# 4. Подсчёт слов
#
# Считать текст из текстового файла.
# Посчитать и вывести количество слов и знаков.
# Сформировать словать, в котором каждому слову
# будет соответствовать количество его повторений в тексте.
PUNCTUATION = ('.', ',', ';', ':', '!', '?', '-')


def get_tokens(text_file):
    tokens = []
    for line in text_file:
        line = line.strip()
        tokens += line.split(' ')
    tokens = [token for token in tokens if token]
    return tokens


def output_statistics(tokens, number_of_signs):
    print u"Количество слов в файле: %d" % len(tokens)
    print u"Количество знаков в файле: %d" % number_of_signs


def get_words(tokens):
    set_words = set(tokens)
    words = {word: 0 for word in set_words}
    for token in tokens:
        words[token] += 1
    return words


def output_words(words):
    for word in words:
        print "%s : %d" % (word, words[word])


if __name__ == "__main__":
    text = open("text.txt", 'r')
    tokens = get_tokens(text)

    i = 0
    number_of_signs = 0
    for token in tokens:
        string = ''
        for t in token:
            if t not in PUNCTUATION:
                string += t
            else:
                number_of_signs += 1
        tokens[i] = string
        i += 1

    output_statistics(tokens, number_of_signs)

    words = get_words(tokens)
    output_words(words)
