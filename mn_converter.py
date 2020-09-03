import csv
import argparse
from io import StringIO

from char_dictionaries import polish_char_dict, czech_char_dict, latin_char_dict, special_char_dict, redundant_char, \
    cyrilic_char_dict, corrupted_char


def re_encode(byte_conv, conv_dict):
    """
    Converts characters in the supplied bytes specified in dictionary keys with values from the dictionary
    :param byte_conv: bytes to convert
    :param conv_dict: dictionairy with chars to convert
    :return: byte
    """
    for key in conv_dict.keys():
        byte_conv = byte_conv.replace(key, conv_dict[key])
    return byte_conv


def write_line_to_csv(line_to_add):
    """
    Write line to csv
    :param line_to_add: line to add
    :return: bool
    """

    saved = True
    with open('csv_encoded.csv', 'a') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        try:
            csv_writer.writerow(line_to_add)
        except csv.Error as e:
            print(e)
            saved = False
    return saved


def csv_converter(filepath):
    """
    Converts corrupted csv from National Museum Kraków to UTF-8 comma separated csv file
    :param filepath: Input filepath
    :return: None
    """
    file_output = 'csv_encoded.csv'
    error_counter = 0
    row_converted = 0
    all_dicts = {**polish_char_dict,
                 **special_char_dict,
                 **redundant_char,
                 **cyrilic_char_dict,
                 **czech_char_dict,
                 **latin_char_dict
                 }

    show_input(filepath)

    with open(filepath, 'rb') as csv_file:
        temp_byte = b''
        csv_lines = csv_file.readlines()
        for i, value in enumerate(csv_lines):
            repaired_bin = re_encode(value, all_dicts)
            # when ä occurs (aL\n)
            if repaired_bin.find(b'aL\n') != -1:
                temp_byte = re_encode(repaired_bin, corrupted_char)
                continue
            if temp_byte:
                repaired_bin = temp_byte + repaired_bin
            temp_byte = b''
            repaired_string = repaired_bin.decode('UTF-8')
            csv_file_io = StringIO(repaired_string)
            csv_reader = csv.reader(csv_file_io, delimiter=';')
            saved = write_line_to_csv(list(csv_reader)[0])
            if saved:
                row_converted += 1
            else:
                error_counter += 1
    show_result(row_converted, error_counter,file_output)


def show_result(row_converted, error_counter,file_output):
    print('Script ended')
    print('Row converted: {}'.format(row_converted))
    print('----')
    print('File saved to: {}'.format(file_output))
    print('----')

    if error_counter:
        print('{} Errors'.format(error_counter))

def show_input(filepath):
    print('----')
    print('File to convert: {}'.format(filepath))
    print('----')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert corrupted csv from MN Krakow')
    parser.add_argument("-i", "--input", help="Path of input file")

    args = parser.parse_args()

    if args.input:
        csv_converter(args.input)
