import sys

class DNASequence:
    def __init__(self, sequence: str):
        self.original_sequence = sequence
        self.compressed_sequence = self.__compress()

    def __compress(self):
        compressed_sequence = 0b00
        for nucleotide in self.original_sequence:
            match nucleotide:
                case 'a':
                    compressed_value = 0b00
                case 'c':
                    compressed_value = 0b01
                case 'g':
                    compressed_value = 0b10
                case 't':
                    compressed_value = 0b11
            
            compressed_sequence <<= 2
            compressed_sequence |= compressed_value
        return compressed_sequence

    def __decompress(self):
        decompressed_sequence = []
        value = self.compressed_sequence
        while value:
            nucleotide_value = value & 0b11
            match nucleotide_value:
                case 0b00:
                    decompressed_sequence.append('a')
                case 0b01:
                    decompressed_sequence.append('c')
                case 0b10:
                    decompressed_sequence.append('g')
                case 0b11:
                    decompressed_sequence.append('t')
            value >>= 2
        return ''.join(decompressed_sequence[::-1])

    def __str__(self):
        return self.__decompress()

if __name__ == '__main__':
    print("1000 нуклеотидов")
    sequence = open('1000.txt').read().replace('\n', '')
    coder = DNASequence(sequence)
    print(f"Исходная последовательность: {sys.getsizeof(coder.original_sequence)} байтов")
    print(f"Сжатая последовательность: {sys.getsizeof(coder.compressed_sequence)} байтов")
    print()

    print("10_000 нуклеотидов")
    sequence = open('10000.txt').read().replace('\n', '')
    coder = DNASequence(sequence)
    print(f"Исходная последовательность: {sys.getsizeof(coder.original_sequence)} байтов")
    print(f"Сжатая последовательность: {sys.getsizeof(coder.compressed_sequence)} байтов")
    print()

    print("100_000 нуклеотидов")
    sequence = open('100000.txt').read().replace('\n', '')
    coder = DNASequence(sequence)
    print(f"Исходная последовательность: {sys.getsizeof(coder.original_sequence)} байтов")
    print(f"Сжатая последовательность: {sys.getsizeof(coder.compressed_sequence)} байтов")
    print()

    print("1_000_000 нуклеотидов")
    sequence = open('1000000.txt').read().replace('\n', '')
    coder = DNASequence(sequence)
    print(f"Исходная последовательность: {sys.getsizeof(coder.original_sequence)} байтов")
    print(f"Сжатая последовательность: {sys.getsizeof(coder.compressed_sequence)} байтов")
    print()

    print("10_000_000 нуклеотидов")
    sequence = open('10000000.txt').read().replace('\n', '')
    coder = DNASequence(sequence)
    print(f"Исходная последовательность: {sys.getsizeof(coder.original_sequence)} байтов")
    print(f"Сжатая последовательность: {sys.getsizeof(coder.compressed_sequence)} байтов")
    print()

