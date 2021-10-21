# -*- coding: utf-8 -*-
import sys
import unicodedata
import re
import random

def read_corpus(trans_filename):
    with open(trans_filename, 'r') as f:
        txt = f.readlines()
    ret = [line.strip().split('\t') for line in txt]
    return ret

jpn = read_corpus('data/eng-jpn_normalized.txt')
chn = read_corpus('data/eng-chn_normalized.txt')
#print(jpn[-3:])
#print(chn[-3:])

MAX_LENGTH = 12

# def filterPair(p):
#     return len(p[0].split(' ')) < MAX_LENGTH and \
#         len(p[1].split(' ')) < MAX_LENGTH and \
#         p[0].startswith(eng_prefixes)

def filterPair(p, max_len=MAX_LENGTH):
    return len(p[0].split(' ')) < max_len and \
        len(p[1].split(' ')) < max_len

def filterPairs(pairs, max_len=MAX_LENGTH):
    return [pair for pair in pairs if filterPair(pair, max_len=max_len)]


SOS_token = 1
EOS_token = 0

class Lang_dict:
    def __init__(self, name):
        self.name = name
        self.wrd2idx = {'EOS':0, 'SOS':1}
        self.wrd2cnt = {}
        self.idx2wrd = {0: "EOS", 1: "SOS"}
        self.n_words = 2  # SOSとEOSをカウント

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.wrd2idx:
            self.wrd2idx[word] = self.n_words
            self.wrd2cnt[word] = 1
            self.idx2wrd[self.n_words] = word
            self.n_words += 1
        else:
            self.wrd2cnt[word] += 1

E2J_dict, J2E_dict = Lang_dict('eng2jpn'), Lang_dict('jpn2eng')
for p in filterPairs(jpn, max_len=MAX_LENGTH):
    E2J_dict.addSentence(p[0])
    J2E_dict.addSentence(p[1])
E2J_pairs = filterPairs(jpn, max_len=MAX_LENGTH)

E2C_dict, C2E_dict = Lang_dict('eng2chn'), Lang_dict('chn2eng')
for p in filterPairs(chn, max_len=MAX_LENGTH):
    E2C_dict.addSentence(p[0])
    C2E_dict.addSentence(p[1])
E2C_pairs = filterPairs(chn, max_len=MAX_LENGTH)

print(f'総語彙数: 英2日:{E2J_dict.n_words}, 日2英:{J2E_dict.n_words}')
print(f'総語彙数: 英2中:{E2C_dict.n_words}, 中2英:{C2E_dict.n_words}')
print(f'出力サンプル {[random.choice(E2J_pairs) for _ in range(5)]}')
print(f'出力サンプル {[random.choice(E2C_pairs) for _ in range(5)]}')
