"""
This function takes a string of DNA, such as 'GTCA', and returns a list containing correctly matched DNA pairs.

The pairs are as follows:

'G' -> 'C'
'C' -> 'G'
'T' -> 'A'
'A' -> 'T'

The function should ignore any letters that are not valid DNA pairs (e.g. not 'G', 'C', 'T' or 'A'). However, it should also work for lowercase and uppercase letters.

dna_pairs('G') # returns ['GC']
dna_pairs('GAT') # returns ['GC', 'AT', 'TA']
dna_pairs('GYTC') # returns ['GC', 'TA', 'CG']
dna_pairs('gat') # returns ['GC', 'AT', 'TA']

"""

def dna_pairs(dna_string):
    # Your code here
    pass


def test_empty_string_produces_empty_list():
    assert dna_pairs('') == []


def test_invalid_letters_ignored():
    assert dna_pairs('B') == []
    assert dna_pairs('z') == []


def test_single_valid_uppercase_returns_correct_pair():
    assert dna_pairs('G') == ['GC']
    assert dna_pairs('C') == ['CG']
    assert dna_pairs('T') == ['TA']
    assert dna_pairs('A') == ['AT']


def test_single_valid_lowercase_returns_correct_uppercase_results():
    assert dna_pairs('g') == ['GC']
    assert dna_pairs('c') == ['CG']
    assert dna_pairs('t') == ['TA']
    assert dna_pairs('a') == ['AT']


def test_long_valid_uppercase_string_returns_valid_list():
    assert dna_pairs('GAT') == ['GC', 'AT', 'TA']


def test_long_uppercase_with_invalid_chars_returns_valid_list():
    assert dna_pairs('GYTC') == ['GC', 'TA', 'CG']


def test_mixed_string_returns_valid_list():
    assert dna_pairs('CGauTzgAcj') == ['CG', 'GC', 'AT', 'TA', 'GC', 'AT', 'CG']

