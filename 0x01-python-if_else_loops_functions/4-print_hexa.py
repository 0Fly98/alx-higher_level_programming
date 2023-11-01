#!/usr/bin/python3

skipped_chars = [101, 113]
alphabet = [chr(character) for character in range(97, 123) if character not in skipped_chars]
print(''.join(alphabet))
