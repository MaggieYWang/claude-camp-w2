#这是一个文本词频统计器，输入一段文字，输出每个单词出现的次数
"""用字典存储统计结果
按出现次数从高到低排序输出
忽略大小写差异"""

import re

text = input("请输入一段文字：")
text_clean = re.sub(r'[^a-zA-Z\s]', '', text)  #把所有标点替换成空字符串（即删除），字母和空格保留不动。
word_list = text_clean.lower().split() 

word_count = {}
for word in word_list:              #遍历 list 里每个单词
    if word not in word_count:      # not in 判断不存在
        word_count[word] = 1
    else:                           # 这个词出现过
        word_count[word] += 1     

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=1)

print("\n词频统计结果如下，已按出现次数从高到低排序")
print("-" * 25)
for item in sorted_words:
    print(item[0], ":", item[1])
