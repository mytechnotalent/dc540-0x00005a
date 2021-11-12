# MIT License
#
# Designer: Kevin Thomas
# Developer: Kevin Thomas
#
# Copyright (c) 2021 My Techno Talent
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class MicroEnigma:
    """
    Class to handle the MicroEnigma engine
    """
    
    def __init__(self, fast_rotor, medium_rotor, slow_rotor):
        """
        Attrs:
            fast_rotor: int
            medium_rotor: int
            slow_rotor: int
        """
         # special thanks to Bradan Lane for the correct rotor and reflector b mappings, check out his Pocket Enigma @ https://www.tindie.com/products/bradanlane/pocket-enigma
        self.fast_rotor_alphabet = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
        self.medium_rotor_alphabet = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
        self.slow_rotor_alphabet = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
        self.reflector_b_alphabet = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
        # computers are zero-indexed, we need to subtract 1, if user selects 1 it becomes 0
        self.fast_rotor = fast_rotor - 1
        self.medium_rotor = medium_rotor - 1
        self.slow_rotor = slow_rotor - 1
        rotors = [self.fast_rotor, self.medium_rotor, self.slow_rotor]
        for rotor in rotors:
            rotor = rotor % 26
        self.fast_rotor = rotors[0]
        self.medium_rotor = rotors[1]
        self.slow_rotor = rotors[2]
        self.reflector = [letter for letter in reversed(self.reflector_b_alphabet)]
        
    def permutate(self, rotor, alphabet):
        """
        Method to re-order the alphabet depending on the rotors settings
        
        Params:
            rotor: int
            alphabet: list
        """
        new_alphabet = ''.join(alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(rotor):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        return new_alphabet
        
    def inverse_permutation(self, rotor, alphabet):
        """
        Method to inverse re-order the alphabet depending on the rotors settings
        
        Params:
            rotor: int
            alphabet: list
        """
        new_alphabet = ''.join(alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(rotor):
            new_alphabet.append(new_alphabet[0])
            new_alphabet.pop(0)
        return new_alphabet

    def cipher(self, text):
        """
        Method to encrypt/decrypt text
        
        Params:
            text: str
        """
        cipher_text = []
        text.split()
        # cipher each letter
        for letter in text:
            # handle empty space to ignore rotor algorithm
            if letter == ' ':
                cipher_text.append(' ')
            else:
                # letter is ciphered by fast rotor
                temp_letter = self.permutate(self.fast_rotor, self.fast_rotor_alphabet)[self.fast_rotor_alphabet.index(letter)]
                # letter is ciphered by medium rotor
                temp_letter = self.permutate(self.medium_rotor, self.medium_rotor_alphabet)[self.medium_rotor_alphabet.index(temp_letter)]
                # letter is ciphered by slow rotor
                temp_letter = self.permutate(self.slow_rotor, self.slow_rotor_alphabet)[self.slow_rotor_alphabet.index(temp_letter)]
                # reflector is returning the inverse of that letter
                temp_letter = self.reflector[self.reflector_b_alphabet.index(temp_letter)]
                # letter is ciphered by slow rotor, inverse algorithm
                temp_letter = self.inverse_permutation(self.slow_rotor, self.slow_rotor_alphabet)[self.slow_rotor_alphabet.index(temp_letter)]
                # letter is ciphered by medium rotor, inverse algorithm
                temp_letter = self.inverse_permutation(self.medium_rotor, self.medium_rotor_alphabet)[self.medium_rotor_alphabet.index(temp_letter)]
                # letter is ciphered by fast rotor, inverse algorithm
                temp_letter = self.inverse_permutation(self.fast_rotor, self.fast_rotor_alphabet)[self.fast_rotor_alphabet.index(temp_letter)]
                # append temp letter to cipher text
                cipher_text.append(temp_letter)
            # rotor rotation algorithm
            self.fast_rotor += 1
            if self.fast_rotor % len(self.fast_rotor_alphabet) == 0:
                self.medium_rotor += 1
                self.fast_rotor = 0
            if self.medium_rotor % len(self.medium_rotor_alphabet) == 0 and self.fast_rotor % len(self.fast_rotor_alphabet) != 0 and self.medium_rotor >= len(
                    self.medium_rotor_alphabet) - 1:
                self.slow_rotor += 1
                self.medium_rotor = 1
        upper_cipher_text = '' 
        for letter in cipher_text: 
            upper_cipher_text += letter  
        return ''.join(upper_cipher_text.upper())


while True:
    try:
        fast_rotor = int(input('FAST ROTOR: '))
        if fast_rotor < 1 or fast_rotor > 26:
            print('Please enter a value from 1 to 26...')
            break
        medium_rotor = int(input('MEDIUM ROTOR: '))
        if medium_rotor < 1 or medium_rotor > 26:
            print('Please enter a value from 1 to 26...')
            break
        slow_rotor = int(input('SLOW ROTOR: '))
        if slow_rotor < 1 or slow_rotor > 26:
            print('Please enter a value from 1 to 26...')
            break
        micro_enigma = MicroEnigma(fast_rotor, medium_rotor, slow_rotor)
        cipher = input('CIPHER: ')
        if not cipher.isupper():
            print('Please enter only capital letters...')
            break
        print('CIPHER: ', end='')
        print(micro_enigma.cipher(cipher))
    except ValueError:
        print('Please enter a value from 1 to 26...')
        break
