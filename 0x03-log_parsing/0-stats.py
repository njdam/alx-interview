#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''

import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.

    Args:
        input_line (str): The line of the HTTP request log.

    Returns:
        dict: A dictionary containing extracted information from the log line.
    '''
    # Define regular expression patterns for each section of the log line
    fp = (
        # Match IP address section: 0 or more whitespace characters,
        # followed by 1 or more non-whitespace characters (captured as 'ip'),
        # followed by 0 or more whitespace characters
        r'\s*(?P<ip>\S+)\s*',
        # Match date section: 0 or more whitespace characters,
        # followed by '[' and the date in the format 'YYYY-MM-DD
        # HH:MM:SS.SSSSSS' (captured as 'date'), followed by ']'
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        # Match request section: 0 or more whitespace characters,
        # followed by '"' and any characters that are not '"' (captured as
        # 'request'), followed by '"', and 0 or more whitespace characters
        r'\s*"(?P<request>[^"]*)"\s*',
        # Match status code section: 0 or more whitespace characters,
        # followed by 1 or more non-whitespace characters
        # (captured as 'status_code')
        r'\s*(?P<status_code>\S+)',
        # Match file size section: 0 or more whitespace characters,
        # followed by 1 or more digits (captured as 'file_size')
        r'\s*(?P<file_size>\d+)'
    )
    # Construct a regular expression pattern for the entire log line
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    # Match the log line against the pattern
    resp_match = re.fullmatch(log_fmt, input_line)
    # Extract relevant information from the match
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size.
        status_codes_stats (dict): A dictionary containing counts of each
            status code.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): A dictionary containing counts of each
            status code.

    Returns:
        int: The new total file size.
    '''
    # Extract relevant information from the log line
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    # Update status code count and total file size
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            # Update metrics for each line of input
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            # Print statistics every 10 lines
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # Print final statistics when interrupted
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
