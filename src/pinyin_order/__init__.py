from pypinyin import lazy_pinyin

__all__ = [
    'PinyinOrderStr',
    'pinyin_sorted'
]


def _is_han(s: str):
    return '\u4e00' <= s <= '\u9fff'


class PinyinOrderStr:

    def __init__(self, string: str, ignore_case=True):
        """
        代理字符串，可进行汉字拼音的大小对比
        :param string: 字符串
        :param ignore_case: 英文字母是否忽略大小写
        """
        self._string = string
        self._ignore_case = ignore_case

    def __iter__(self):
        return str.__iter__(self._string)

    def _comp_format(self, x, y):
        if _is_han(x) and _is_han(y):
            x, y = lazy_pinyin(x)[0], lazy_pinyin(y)[0]
        elif self._ignore_case:
            x, y = x.lower(), y.lower()
        return x, y

    def _comp(self, other, reversal=False):
        xv = iter(self)
        yv = iter(other)
        if reversal:
            xv, yv = yv, xv

        while True:
            try:
                x = next(xv)
            except StopIteration:
                x = ''
            try:
                y = next(yv)
            except StopIteration:
                y = ''
            if x == '' or y == '':
                return x > y
            x, y = self._comp_format(x, y)
            if x != y:
                return x > y

    def __gt__(self, other: 'PinyinOrderStr'):
        return self._comp(other)

    def __ge__(self, other: 'PinyinOrderStr'):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other: 'PinyinOrderStr'):
        return self._comp(other, True)

    def __le__(self, other: 'PinyinOrderStr'):
        return self.__lt__(other) or self.__eq__(other)

    def __eq__(self, other: 'PinyinOrderStr'):
        xv = iter(self)
        yv = iter(other)

        while True:
            try:
                x = next(xv)
            except StopIteration:
                x = ''
            try:
                y = next(yv)
            except StopIteration:
                y = ''
            x, y = self._comp_format(x, y)
            if x != y:
                return False
            if x == '':
                # 等价于: x == '' and y == ''
                return True


def pinyin_sorted():
    ...
