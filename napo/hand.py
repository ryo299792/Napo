#!/usr/bin/env python
# coding: UTF-8

# Cardクラス
import card
# リストの要素をシャッフル
from random import shuffle


class Hand:
    """
    52枚のトランプカード（1デッキ）を作成
    Attributes
    ----------
    deck_set_no : int
        デッキの個数
    """

    def __init__(self, list ):
        """
        Parameters
        ----------
        deck_set_count : int
            デッキの個数
        """

        self.cards = list
        #for index in range(list):
        #    self.cards.append(card.Card(index))
        # デッキをシャッフル
        self.cards.sort()

    def print_hand(self):
        for i in self.cards:
            print(i,end=",")
        print()
        print("------")

    def get_card(self, card_num=1):
        """
        要素を取得しリストから削除
        Parameters
        ----------
        card_num : int
            取得するカードの枚数
        """

        self.card_list = []
        if len(self.cards) == 0:
            # カードが0枚の時は何もしない
            return

        # self.cards内の末尾からcard_num分取得しリストから削除
        for index in range(card_num):
            self.card_list.append(self.cards.pop())
        return self.card_list
