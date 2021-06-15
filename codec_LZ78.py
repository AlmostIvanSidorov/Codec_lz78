# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:00:01 2021

@author: Sidorov
"""

import sys


def encoder(uncomp_data):
    word, result, wordbyte = bytearray(), bytearray(), bytearray()
    byte_chr = bytearray(b'1')
    dictionary = {}
    dict_ind = 1
    for byte in uncomp_data:
        byte_chr.pop()
        byte_chr.append(byte)
        wordbyte = word + byte_chr
        wordbyte_tuple = tuple(wordbyte)
        word_tuple = tuple(word)
        if wordbyte_tuple in dictionary:
            word = wordbyte
        else:
            if wordbyte == byte_chr:
                result.append(0)
                result.append(byte)
            else:
                result.append(dictionary[word_tuple])
                result.append(byte)
            dictionary[wordbyte_tuple] = dict_ind
            dict_ind += 1
            word = bytearray()
            if dict_ind > 251:
                result.append(253)
                dict_ind = 0
                dictionary = {}
                dict_ind = 1
    for byte2 in word:
        result.append(0)
        result.append(byte2)
    return result


def decoder(comp_data):
    result = bytearray()
    dictionary = {}
    dict0 = bytearray()
    dict0_tuple = tuple(dict0)
    dictionary = {0: dict0_tuple}
    dict_ind = 1
    word = bytearray()
    byte_chr = bytearray(b'1')
    i = 0
    while i < (len(comp_data)):
        if int(comp_data[i]) == 253:
            i = i+1
            dictionary = {}
            dictionary = {0: dict0_tuple}
            dict_ind = 1
        else:
            byte_chr.pop()
            byte_chr.append(comp_data[i+1])
            word = bytearray(dictionary[int(comp_data[i])]) + byte_chr
            word_tuple = tuple(word)
            dictionary[dict_ind] = word_tuple
            dict_ind += 1
            for byte2 in word:
                result.append(byte2)
            i = i + 2
    return result


if len(sys.argv) <= 1:
    data = sys.stdin.buffer.read()
    data_LZ78_lz = encoder(data)
    sys.stdout.buffer.write(data_LZ78_lz)
else:
    if sys.argv[1] == '-d':
        data = sys.stdin.buffer.read()
        data_LZ78 = decoder(data)
        sys.stdout.buffer.write(data_LZ78)
    else:
        print('ErrorS')
