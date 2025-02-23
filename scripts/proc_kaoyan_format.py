import json

with open('json/5-考研-顺序.json') as f:
    words = json.load(f)

with open('json/5-kaoyan-indent.json', 'w') as f:
    json.dump(words, f, indent=2, ensure_ascii=False)

# 去除words 中的重复单词，保留第一个出现的单词，其余的删除
# 输出重复词信息。
words_dict = {}
repeat_words = []
for word in words:
    if word['word'] in words_dict:
        print("repeat word: ", word['word'])
        repeat_words.append(word)
    else:
        words_dict[word['word']] = word

print("repeat words: ", len(repeat_words))
words = list(words_dict.values())
with open('json/5-kaoyan-indent-no-repeat.json', 'w') as f:
    json.dump(words, f, indent=2, ensure_ascii=False)


# 输出首字母是大写字母的单词
words_capital = []
for word in words:
    if word['word'][0].isupper():
        words_capital.append(word['word'])
print("capital words: ", len(words_capital))
with open('json/5-kaoyan-indent-capital.json', 'w') as f:
    json.dump(words_capital, f, indent=2, ensure_ascii=False)
        


