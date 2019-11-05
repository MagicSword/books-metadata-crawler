#encoding=utf-8
import jieba

sentence = "鼓，可以傳遞訊息、也是一種節奏樂器，在台灣無論是神將團、八家將、官將首、布袋戲這些傳統藝陣技藝項目，還是紅白喜事民俗活動，鼓聲都是不可或缺的重要元素，今天咱們要跟著祖傳三代的製鼓世家來「講鼓」，講「鼓」早的故事、製鼓的辛苦，聽鼓聲傳千里，振作精神勇往直前！"
print("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
print("Output 精確模式 Full Mode：")
for word in words:
    print(word)
"""
sentence = "独立音乐需要大家一起来推广，欢迎加入我们的行列！"
print("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
print("Output 精確模式 Full Mode：")
for word in words:
    print(word)
"""    
