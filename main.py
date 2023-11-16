win_file = 'win.txt'
wout_file = 'wout.txt'
word_file = 'words.txt'

sin_file = 'sin.txt'
sout_file = 'sout.txt'


# --------------------------------------------------
def add_new_word(filename):
    """ Words """

    list_of_words = []
    list_n_word = []
    list_3_word = []
    list_4_word = []
    list_5_word = []

    # read from file and parse into List
    with open(wout_file) as file_word:
        for line in file_word:
            for w in line.split():
                if w in list_of_words:
                    print("已存在: \t", w)
                else:
                    list_of_words.append(w)
            for w in line.split():
                if len(w) == 3:
                    list_3_word.append(w)
                if len(w) == 4:
                    list_4_word.append(w)
                if len(w) == 5:
                    list_5_word.append(w)

    with open(win_file) as file_word:
        for line in file_word:
            for w in line.split():
                if w in list_of_words:
                    print("已存在: \t", w)
                else:
                    print("新单词: \t", w)
                    list_of_words.append(w)

    # ask for new word
    while True:
        new_word = input("请输入新单词【Q-退出】：")
        if new_word == 'Q':
            break
        if new_word in list_of_words:
            print("已存在: \t", new_word)
        else:
            print("新单词: \t", new_word)
            list_of_words.append(new_word)

    list_of_words.sort()
    list_n_word.sort()

    for n, i in enumerate(list_of_words):
        if i in ['a-b-c-d', 'e-f-g', 'h-i-j-k', 'l-m-n', 'o-p-q', 'r-s-t', 'u-v-w-x-y-z']:
            list_of_words[n] = '\r\n### ' + i + '\r\n'

    list_of_words.remove('###')
    # print(list_of_words)

    # write to file
    with open(wout_file, 'w') as file_word:
        file_word.write(' '.join(list_of_words))

    with open(word_file, 'w') as file_word:
        file_word.write(','.join(list_n_word))
        file_word.write('\r\n')
        file_word.write(','.join(list_3_word).replace('###', ''))
        file_word.write('\r\n')
        file_word.write(','.join(list_4_word))
        file_word.write('\r\n')
        file_word.write(','.join(list_5_word))


# --------------------------------------------------
def sorting(filename):
    """ Sentences """

    infile = open(filename, encoding='UTF-8')
    lines = []
    lastline = ''

    for line in infile:
        temp = line.split('\n')
        for i in temp:
            lines.append(i)
    infile.close()

    lines.sort()

    outfile = open(sout_file, "w", encoding='UTF-8')
    for l in lines:
        if lastline == l:
            continue
        if lastline.__len__() > 0 and lastline[0].lower() != l[0].lower():
            outfile.writelines("\n\n")
        outfile.writelines(l)
        outfile.writelines("\n")
        lastline = l
    outfile.close()


# --------------------------------------------------
def main():
    """ main """

    # add_new_word(win_file)
    sorting(sin_file)


# --------------------------------------------------
if __name__ == '__main__':
    main()
