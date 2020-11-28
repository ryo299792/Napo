#!/usr/bin/env python
# coding: UTF-8

class Card:
    """
    カードのマークと数字を出力
    Attributes
    ----------
    card_mark : int
        カードのマーク（♠︎❤︎♦︎♣︎）
    card_value : int
        カードの数字
    """
    # マーク
    #MARKS = ("♠︎-", "❤︎-", "♦︎-", "♣️-")
    MARKS = ("♠️ ", "❤️ ", "♦️ ", "♣️ ")
    # 数字
    #VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    VALUES = (" A"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"," J"," Q", " K")

    def __init__(self, card_mark, card_value):
        """
        Parameters
        ----------
        card_mark : int
            カードのマーク（♠︎❤︎♦︎♣︎）
        card_value : int
            カードの数字
        """
        self.mark = card_mark
        self.value = card_value

    # オーバーライドしてインスタンスの出力内容を変更
    def __repr__(self):
        if self.mark == 4 :
            return "🃏 " + str(self.value)
        else :
            return self.MARKS[self.mark] + str(self.VALUES[self.value])

    def __lt__(self, other):
        if self.mark == other.mark :
            return self.value < other.value
        else :
            return self.mark < other.mark

    def __ge__(self, other):
        if self.mark == other.mark :
            return self.value > other.value
        else :
            return self.mark > other.mark
