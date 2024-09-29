from read_utils import *

def scan_duplicate(x):
    x_ = set(list(x.keys()))
    if len(x) == len(x_):
        print('No duplicates found.')
    else:
        print('List contains duplicates')


def build_vocab():
    specials = ['<pad>', '<bos>', '<eos>', '<sep>', '<unk>']

    # Create input and output vocabularies
    input_vocab = specials + read_age() + read_sex() + read_evidences()
    output_vocab = specials + read_conditions()

    # Create mappings from token to index
    input_vocab = {key: value for value, key in enumerate(input_vocab)}
    output_vocab = {key: value for value, key in enumerate(output_vocab)}

    # Assert that all indices are valid
    assert all(value < len(input_vocab) for value in input_vocab.values()), "Input vocab values out of range!"
    assert all(value < len(output_vocab) for value in output_vocab.values()), "Output vocab values out of range!"

    return input_vocab, output_vocab


if __name__ == '__main__':
    in_vocab, out_vocab = build_vocab()

    scan_duplicate(in_vocab)
    scan_duplicate(out_vocab)
    print('')

    print(in_vocab)
    print(out_vocab)
    print(len(in_vocab))
    print(len(out_vocab))
    print('')

    # Test tokenization
    line = '<bos> age_15-29 <sep> F <sep> douleurxx_carac lancinante_/_choc_électrique <eos> <pad>'.split(' ')
    s2i = list(map(lambda x: in_vocab.get(x, in_vocab['<unk>']), line))
    print(s2i)

    line = '<bos> Bronchite RGO Possible_NSTEMI_/_STEMI Angine_instable <eos> <pad> <pad>'.split(' ')
    s2i = list(map(lambda x: out_vocab.get(x, out_vocab['<unk>']), line))
    print(s2i)

    # Check if the converted indices are valid
    for token in line:
        if token not in in_vocab:
            print(f"Warning: Token '{token}' not in input vocabulary.")
    
    for token in line:
        if token not in out_vocab:
            print(f"Warning: Token '{token}' not in output vocabulary.")
