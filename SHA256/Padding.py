def padding(message):



    original_len = len(message) * 8  # to obtain length in bytes
    message = int.from_bytes(message, "big")

    message = (message << 1) | 1  # adding '1' bit to the end
    current_length = original_len + 1

    while current_length % 512 != 448:  # padding of other 447 bits with '0's
        message <<= 1
        current_length += 1

    message = (message << 64) | original_len  # adding message's length in 64 bits big int format
    original_len += 64
    return message
