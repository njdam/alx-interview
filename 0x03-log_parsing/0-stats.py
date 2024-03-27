#!/usr/bin/python3
import sys

total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    """
    Below line iterates over the lines from the standard input `sys.stdin`
    using `enumerate`, which provide index `i` along with each line `line`.
    The second argument of enumerate sets the start index to 1.
    """
    for i, line in enumerate(sys.stdin, 1):
        try:
            """
            These lines split the input line into a list of strings using
            whitespace as the delimiter (`split()`), then extract the status
            code and file size from the last two elements of the list
            (`data[-2]` and `data[-1]`, respectively),
            converting them to integers.
            """
            data = line.split()
            status_code = int(data[-2])
            file_size = int(data[-1])

            """
            These lines update the `total_size` by adding the `file_size`,
            and increment the count of the corresponding `status_code`
            in the `status_count` dictionary.
            """
            total_size += file_size
            status_count[status_code] += 1

            """
            This block executes when the line count (`i`) is a multiple
            of `10`. It prints the `total_size` and iterates over items
            in the `status_count` dictionary, printing each status code
            and its count, sorted in ascending order.
            """
            if i % 10 == 0:
                print(f"File size: {total_size}")
                for code, count in sorted(status_count.items()):
                    if count:
                        print(f"{code}: {count}")
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code, count in sorted(status_count.items()):
        if count:
            print(f"{code}: {count}")
