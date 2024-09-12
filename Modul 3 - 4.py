def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower().count(root_word.lower()) or i.lower() in root_word.lower():
            same_words.append(i)
    print (f'Слово "{root_word}" имеет общий корень со словами: {same_words}')
    return same_words
single_root_words('RICH', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'DISABLE', 'Bagel')