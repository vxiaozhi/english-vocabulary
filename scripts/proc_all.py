import json

files_map = {
    "junior": 'json/1-初中-顺序.json',
    "senior": 'json/2-高中-顺序.json',
    "cet4": 'json/3-cet4-顺序.json',
    "cet6": 'json/4-CET6-顺序.json',
    "postgrad": 'json/5-考研-顺序.json',
    "toefl": 'json/6-托福-顺序.json',
}

global_words_dict = {}
global_capital_words = []

def add_word_to_global_dict(word):
    if word['word'] not in global_words_dict:
        word['seq'] = len(global_words_dict)
        global_words_dict[word['word']] = word

    if word['word'][0].isupper() and word['word'] not in global_capital_words:
        global_capital_words.append(word['word'])
def proc_one(file):
    with open(file) as f:
        words = json.load(f)

    indent_file = file.replace('顺序', 'indent')
    with open(indent_file, 'w') as f:
        json.dump(words, f, indent=2, ensure_ascii=False)

    # 去除words 中的重复单词，保留第一个出现的单词，其余的删除
    # 输出重复词信息。
    words_dict = {}
    repeat_words = []
    for word in words:
        if word['word'] in words_dict:
            #print("repeat word: ", word['word'])
            repeat_words.append(word)
        else:
            words_dict[word['word']] = word
        add_word_to_global_dict(word)
        


    print("repeat words: ", len(repeat_words))
    words = list(words_dict.values())
    no_repeat_file = file.replace('顺序', 'indent-no-repeat')
    with open(no_repeat_file, 'w') as f:
        json.dump(words, f, indent=2, ensure_ascii=False)


    # 输出首字母是大写字母的单词
    words_capital = []
    for word in words:
        if word['word'][0].isupper():
            words_capital.append(word['word'])
    print("capital words: ", len(words_capital))
    capital_file = file.replace('顺序', 'indent-capital')
    with open(capital_file, 'w') as f:
        json.dump(words_capital, f, indent=2, ensure_ascii=False)
    
    return list(words_dict.keys())

def proc_all(files_map):
    k_dict = {}
    for k, file in files_map.items():
        print("processing: ", file)
        word_name_list = proc_one(file)
        k_dict[f"{k}_words"] = word_name_list
    
    with open('json/global-words.json', 'w') as f:
        content = {
            'capital': global_capital_words,
            'words': list(global_words_dict.values())
        }
        #print(k_dict)
        content.update(k_dict)
        json.dump(content, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    proc_all(files_map)
            


