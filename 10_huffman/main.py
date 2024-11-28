import heapq
import os


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For the priority queue to work on HuffmanNode
    def __lt__(self, other):
        return self.freq < other.freq


def get_frequency(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def build_huffman_tree(frequency):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return heapq.heappop(priority_queue)


def assign_codes(node, prefix="", code={}):
    if node is not None:
        if node.char is not None:
            code[node.char] = prefix
        assign_codes(node.left, prefix + "0", code)
        assign_codes(node.right, prefix + "1", code)
    return code


def huffman_encoding(data):
    frequency = get_frequency(data)
    root = build_huffman_tree(frequency)
    huffman_codes = assign_codes(root)
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes


def huffman_decoding(encoded_data, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_output = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_output += reverse_codes[current_code]
            current_code = ""
    return decoded_output


# Example usage
data = "this is an example of a huffman tree"
encoded_data, codes = huffman_encoding(data)
decoded_data = huffman_decoding(encoded_data, codes)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
