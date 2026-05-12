from turtledemo.bytedesign import Designer

import pytest
from deck import Card,Deck

def test_shuffle():
    deck = Deck()
    deck.shuffle()
    check = True
    for c in deck.items:
        if not c in deck.new_deck:
            check = False
    assert deck.items != deck.new_deck
    assert len(deck.items) == len(deck.new_deck)
    assert check

def test_draw():
    deck = Deck()
    for _ in range(len(deck)):
        card = deck.items[-1]
        assert card == deck.draw()
    assert len(deck) == 0

def test_reset():
    deck = Deck()
    deck.shuffle()
    deck.reset()
    assert deck.items == Deck.new_deck

def test_getitem():
    deck = Deck()
    check = True
    for i in range(len(deck)):
        if deck.items[i] != deck[i]:
            check = False
    assert check