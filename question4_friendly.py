input_words = ['car', 'cheating', 'dale', 'deal', 'lead', 'listen', 'silent', 'teaching']

def friendlyWords(input_words):
    while input_words != []:
        temp = input_words
        output = []
        for word in temp:
            if sorted(input_words[0]) == sorted(word) and input_words[0] != word:
                if output == []:
                    output.append(input_words[0])
                    output.append(word)
                else:
                    output.append(word)

        if output != []:
            for word in output:
                input_words.remove(word)
            print(' '.join(map(str, output)))
        else: 
            input_words.remove(input_words[0])

friendlyWords(input_words)