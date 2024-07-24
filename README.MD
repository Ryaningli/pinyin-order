# pinyin-order

包含中文的字符串使用拼音比较大小，可用于使用拼音排序字符串等的需求。

```python
from pinyin_order import PinyinOrderStr, pinyin_sorted


result1 = PinyinOrderStr('汉字和English') == PinyinOrderStr('汉子和english')  # True
result2 = PinyinOrderStr('汉字') > PinyinOrderStr('hanzi')  # True
result3 = PinyinOrderStr('abc啊') <= PinyinOrderStr('ABC哦')  # True

strings = ['a哦', 'a啊', '汉字', '这是abc', '者时ABC', '123', 'abc', '漢字', '🏀🐔🏀', ' ']
result4 = pinyin_sorted(strings)
# [' ', '123', 'abc', 'a啊', 'a哦', '汉字', '漢字', '这是abc', '者时ABC', '🏀🐔🏀']
```