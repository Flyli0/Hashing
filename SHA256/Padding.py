def padding(message):
    length = len(message) * 8  # to obtain length in bytes
    original_len = length

    message = message.encode("utf-8")
    message = int.from_bytes(message, "big")

    message = (message << 1) | 1  # adding '1' bit to the end
    length += 1

    while length % 512 != 448:  # padding of other 447 bits with '0's
        message <<= 1
        length += 1

    message = (message << 64) | original_len  # adding message's length in 64 bits big int format
    original_len += 64
    return message

