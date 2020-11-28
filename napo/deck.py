#!/usr/bin/env python
# coding: UTF-8

# Cardクラス
import card
# リストの要素をシャッフル
from random import shuffle


class Deck:
    """
    52枚のトランプカード（1デッキ）を作成
    Attributes
    ----------
    deck_set_no : int
        デッキの個数
    """

    def __init__(self, deck_set_count=1):
        """
        Parameters
        ----------
        deck_set_count : int
            デッキの個数
        """

        self.cards = []
        for index in range(deck_set_count):
            # 4つのマーク
            for mark in range(len(card.Card.MARKS)):
                # 数字（2から13 + 1の14）
                for value in range(len(card.Card.VALUES)):
                    # cardsに追加
                    self.cards.append(card.Card(mark, value))
            #ジョーカ2枚追加
            self.cards.append(card.Card(4,1))
            self.cards.append(card.Card(4,2))
        # デッキをシャッフル
        shuffle(self.cards)

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
