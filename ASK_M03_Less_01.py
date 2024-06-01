def single_root_words(root_word, *other_words):
    print('\troot_word = ', root_word, '\t\tother_words = ', other_words)
    same_words = []
    root_word_lower = root_word.lower()
    for i in range(len(other_words)):
        other_word = other_words[i]
        if same_words_true_or_false(root_word_lower, other_word):
            same_words.append(other_words[i])
    return same_words


def same_words_true_or_false(root_word_lower, other_word):
    other_word_lower = other_word.lower()
    result = ((other_word_lower.count(root_word_lower) != 0) or
              (root_word_lower.count(other_word_lower) != 0))
    return result


result1 = single_root_words('rich', 'richiest',
                            'orichalcum', 'cheers', 'richies', 'Ramir', 'Richard')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Abl', 'Able',
                            'Mable', 'Disable', 'Bagel', 'ablom', 'root', 'dableRich')
print('\n\tresult1 = ', result1)
print('\tresult2 = ', result2)
print('\tresult3 = ', result3)
