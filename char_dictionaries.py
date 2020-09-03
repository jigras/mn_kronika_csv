from collections import UserDict


class CharDict(UserDict):
    def show_chars(self):
        print(self.values())


polish_char_dict = {
    b'E\x1b': b'\xc5\x9b',
    b'E:': b'\xc5\xba',
    b'E;': b'\xc5\xbb',
    b'E9': b'\xc5\xb9',
    b'E<': b'\xc5\xbc',
    b'E\x1a': b'\xc5\x9a',
    b'E\x01': b'\xc5\x81',
    b'E\x02': b'\xc5\x82',
    b'E\x03': b'\xc5\x83',
    b'E\x04': b'\xc5\x84',
    b'D\x04': b'\xc4\x84',
    b'D\x05': b'\xc4\x85',
    b'D\x06': b'\xc4\x86',
    b'D\x07': b'\xc4\x87',
    b'D\x08': b'\xc4\x88',
    b'D\x18': b'\xc4\x98',
    b'oL\x01': b'\xc3\xb3',
    b'L(\xc5\x82':b'\xc5\x82',
    b'zL\x07':b'\xc5\xbc',
    b'eL(':b'\xc4\x99',
    b'aL(':b'\xc4\x85'

}

czech_char_dict = {
    b'D\x0c': b'\xc4\x8c',
    b'D\x0d': b'\xc4\x8d',
    b'D<': b'\xc4\xbc',
    b'D>': b'\xc4\xbe'

}

latin_char_dict = {
    b'C<': b'\xc3\xbc',
    b'C>': b'\xc3\xbe',
    b'C\x06': b'\xc3\x86',
    b'C\x13': b'\xc3\x93',
    b'C\x16': b'\xc3\x96',
    b'aL\x08': b'a\xcc\x88',
}
special_char_dict = {
    b'b\u13\u13': b'\xe2\x80\x93',
    b'b\x00\x13': b'\xe2\x80\x93',
    b'b\x00\x1d': b'\xe2\x80\x9d',
    b'b\x00\x1e': b'\xe2\x80\x9e',
    b'\x00\x19': b'\xe2\x80\x99',
    b'b\x00&': b'\xe2\x80\xa6',
    b'b\x00\x12': b'\xe2\x80\x92',
    b'b\x00\x14': b'\xe2\x80\x94',
    b'b\x00\x11': b'\xe2\x80\x93',
    b'b\x00\x1c': b'\xe2\x80\x9c'

}

redundant_char = {
    b'o;?': b''
}

cyrilic_char_dict = {
    b'Q\x00': b'\xd1\x80',
    b'Q\x01': b'\xd1\x81',
    b'Q\x02': b'\xd1\x82',
    b'Q\x03': b'\xd1\x83',
    b'Q\x04': b'\xd1\x84',
    b'Q\x05': b'\xd1\x85',
    b'Q\x06': b'\xd1\x86',
    b'Q\x0c': b'\xd1\x8c',
    b'P:': b'\xd0\xba',
    b'P;': b'\xd0\xbb',
    b'P<': b'\xd0\xbc',
    b'P>': b'\xd0\xbe',
    b'P?': b'\xd0\xbf',
    b'P!': b'\xd0\xa1',
    b'P0': b'\xd0\xb0',
    b'P1': b'\xd0\xb1',
    b'P2': b'\xd0\xb2',
    b'P3': b'\xd0\xb3',
    b'P4': b'\xd0\xb4',
    b'P5': b'\xd0\xb5',
    b'P6': b'\xd0\xb6',
    b'P7': b'\xd0\xb7',
    b'P8': b'\xd0\xb8',
    b'P9': b'\xd0\xb9',

}

corrupted_char ={
    b'aL\n': b'a\xcc\x88'
}