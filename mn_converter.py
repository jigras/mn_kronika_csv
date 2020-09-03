import csv
import argparse
from io import StringIO

from char_dictionaries import polish_char_dict, czech_char_dict, latin_char_dict, special_char_dict, redundant_char, \
    cyrilic_char_dict, corrupted_char


def re_encode(byte_conv, conv_dict):
    """
    Converts characters in the supplied bytes specified in dictionary keys with values from the dictionary
    :param byte_onv:
    :param conv_dict:
    :return: byte
    """
    for key in conv_dict.keys():
        byte_conv = byte_conv.replace(key, conv_dict[key])
    return byte_conv


def csv_converter(filepath):
    """
    Converts corrupted csv from National Museum Kraków to UTF-8 comma separated csv file
    :param filepath: str
    :return:
    """
    error_counter = 0
    all_dicts = {**polish_char_dict,
                 **special_char_dict,
                 **redundant_char,
                 **cyrilic_char_dict,
                 **czech_char_dict,
                 **latin_char_dict
                 }

    with open(filepath, 'rb') as csv_file:
        temp_byte = b''
        csv_lines = csv_file.readlines()
        for i, value in enumerate(csv_lines):
            repaired_bin = re_encode(value, all_dicts)
            # when ä occurs it
            if repaired_bin.find(b'aL\n') != -1:
                temp_byte = re_encode(repaired_bin, corrupted_char)
                continue
            if temp_byte:
                repaired_bin = temp_byte + repaired_bin
            temp_byte = b''
            repaired_string = repaired_bin.decode('UTF-8')
            csv_file_io = StringIO(repaired_string)
            csv_reader = csv.reader(csv_file_io, delimiter=';')
            with open('csv_encoded.csv', 'a') as new_file:
                csv_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                try:
                    csv_writer.writerow(list(csv_reader)[0])
                except csv.Error as e:
                    print(e)
                    error_counter += 1

    if error_counter:
        print('{} Errors'.format(error_counter))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert corrupted csv from MN Krakow')
    parser.add_argument("-i", "--input", help="Path of input file")

    args = parser.parse_args()

    if args.input:
        csv_converter(args.input)