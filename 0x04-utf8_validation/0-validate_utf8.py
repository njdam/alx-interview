#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # If this byte is part of a multi-byte UTF-8 character
        if num_bytes == 0:
            # Count the number of leading '1' bits to determine
            # the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If this is a single-byte UTF-8 character or an invalid
            # multi-byte UTF-8 character
            if num_bytes == 0:
                continue

            # If the number of bytes in the UTF-8 character is greater
            # than 4 or equal to 1, it's invalid
            if num_bytes > 4 or num_bytes == 1:
                return False

            # Decrement num_bytes to account for the current byte
            num_bytes -= 1
        else:
            # If this byte is not part of a multi-byte UTF-8 character,
            # return False
            if not (byte >> 6 == 0b10):
                return False
            # Decrement num_bytes to track remaining bytes in the current
            # UTF-8 character
            num_bytes -= 1

    # If all bytes have been processed and there are no remaining bytes
    # in the current UTF-8 character
    return num_bytes == 0
