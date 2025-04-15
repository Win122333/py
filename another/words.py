def take_all_words_where_vowels_more_consonants(text):
    def is_vowels_more_consonants(word):
        count = 0
        for i in word:
            if i.lower() in 'аоуиэы':
                count += 1
        return count >= len(word) - count


    answer = set()
    list_of_words = text.split()
    for word in list_of_words:
        if is_vowels_more_consonants(word):
            answer.add(word)
    return list(answer)


def reverse_all_words(text):
    answer = []
    list_of_words = text.split()
    for word in list_of_words:
        answer.append(word[::-1])
    return ' '.join(answer)


def take_all_words_with_len(text, size):
    answer = []
    list_of_words = text.split()
    for word in list_of_words:
        if len(word) == size:
            answer.append(word)
    return answer


def take_all_email(text):
    def is_email(word):
        fl_pr = False
        fl_af = False
        fl_sb = False
        for i in word:
            if i.lower() not in 'qwertyuiopasdfghjklzxcvbnm1234567089_-@':
                return False
            if i in 'qwertyuiopasdfghjklzxcvbnm1234567089_-' and fl_pr == False:
                fl_pr = True
            if i == '@' and fl_pr:
                fl_sb = True
            if i in 'qwertyuiopasdfghjklzxcvbnm1234567089_-' and fl_sb:
                fl_af = True
        return fl_pr and fl_sb and fl_af

    answer = []
    list_of_words = text.split()
    for word in list_of_words:
        if is_email(word):
            answer.append(word)
    return answer


def main():
    with open('text.txt') as f:
        text = ' '.join(f.readlines())
    print(take_all_words_where_vowels_more_consonants(text))


if __name__ == '__main__':
    main()
