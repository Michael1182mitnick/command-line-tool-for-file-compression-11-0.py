# Command-Line_Tool_for_File_Compression
# Develop a command-line tool that can compress and decompress files using various algorithms like Huffman Coding or LZW.
# LZW (Lempel-Ziv-Welch) Algorithm

def lzw_compress(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Initialize the dictionary with single characters
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256

    w = ""
    compressed_data = []

    for char in content:
        wc = w + char
        if wc in dictionary:
            w = wc
        else:
            compressed_data.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = char

    if w:
        compressed_data.append(dictionary[w])

    # Save the compressed data
    compressed_file = file_path + ".lzw"
    with open(compressed_file, 'wb') as f:
        for data in compressed_data:
            f.write(data.to_bytes(2, byteorder='big'))

    print(f"File compressed to {compressed_file}")

# Decompress an LZW compressed file


def lzw_decompress(file_path):
    with open(file_path, 'rb') as f:
        compressed_data = []
        while byte := f.read(2):
            compressed_data.append(int.from_bytes(byte, byteorder='big'))

    # Initialize the dictionary with single characters
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256

    w = chr(compressed_data.pop(0))
    decompressed_data = [w]

    for k in compressed_data:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Invalid compressed data")

        decompressed_data.append(entry)

        # Add new entry to the dictionary
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry

    # Save the decompressed data
    decompressed_file = file_path.replace(".lzw", "_decompressed.txt")
    with open(decompressed_file, 'w') as f:
        f.write(''.join(decompressed_data))

    print(f"File decompressed to {decompressed_file}")
