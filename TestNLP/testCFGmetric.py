#!/usr/bin/python



test_grammar=nltk.CFG.fromstring("""
S -> NP VP
NP -> DT N | NP PP
PP -> PRP NP
VP -> V NP | VP PP
DT -> 'a' | 'the'
N -> 'child' | 'cake' | 'fork'
PRP -> 'with' | 'to'
V -> 'saw' | 'ate'
""")


temp="S->NP VP
NP->DT N | NP PP
PP->PRP NP
VP->V NP | VP PP
DT->'a' | 'the'
N->'child' | 'cake' | 'fork'
PRP->'with' | 'to'
V->'saw' | 'ate'
"""
