import logging
import csv
import argparse
from io import StringIO

from char_dictionaries import polish_char_dict, czech_char_dict, latin_char_dict, \
    special_char_dict, redundant_char, cyrillic_char_dict, corrupted_char

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('convert.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())


def re_encode(byte_conv, conv_dict):
    """
    Converts characters in the supplied bytes specified in dictionary keys with values
    from the dictionary
    :param byte_conv: bytes to convert
    :param conv_dict: dictionairy with chars to convert
    :return: byte
    """
    for key in conv_dict.keys():
        byte_conv = byte_conv.replace(key, conv_dict[key])
    return byte_conv


def write_line_to_csv(line_to_add, file_output):
    """
    Write line to csv
    :param line_to_add: line to add
    :param file_output: name of output file
    :return: bool
    """
    saved = True
    with open(file_output, 'a', encoding='UTF-8') as new_file:
        csv_writer = csv.writer(new_file,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        try:
            csv_writer.writerow(line_to_add)
        except csv.Error as e:
            logger.error(e, exc_info=True)
            saved = False
    return saved


def stream_lines(file_path):
    """
    Splits file into smaller parts, yields file lines
    :param file_name: filepath
    :return: generator object
    """
    file = open(file_path, 'rb')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        yield line


def show_result(row_converted, error_counter, file_output):
    """
    Logs end of script
    :param row_converted: number of row converted
    :param error_counter: number of error while converting
    :param file_output: file output name
    :return: None
    """
    logger.info('Script ended')
    logger.info('Row converted: {}'.format(row_converted))
    logger.info('File saved to: {}'.format(file_output))
    if error_counter:
        logger.error('{} Errors - check log file'.format(error_counter))


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
                 **cyrillic_char_dict,
                 **czech_char_dict,
                 **latin_char_dict
                 }

    logger.info('File to convert: {}'.format(filepath))
    temp_byte = b''
    for value in stream_lines(filepath):
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
        csv_row = list(csv_reader)[0]
        saved = write_line_to_csv(csv_row, file_output)
        if saved:
            row_converted += 1
        else:
            error_counter += 1

    show_result(row_converted, error_counter, file_output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert corrupted csv from MN Krakow')
    parser.add_argument("-i", "--input", help="Path of input file", required=True)

    args = parser.parse_args()
    if args.input:
        csv_converter(args.input)
