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


class MicroCipher:
    """
    Class to handle the MicroCipher engine
    """
    
    def __init__(self, fast_wheel, medium_wheel, slow_wheel):
        """
        Attrs:
            fast_wheel: int
            medium_wheel: int
            slow_wheel: int
        """
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        # computers are zero-indexed, we need to subtract 1, if user selects 1 it becomes 0
        self.fast_wheel = fast_wheel - 1
        self.medium_wheel = medium_wheel - 1
        self.slow_wheel = slow_wheel - 1
        wheels = [self.fast_wheel, self.medium_wheel, self.slow_wheel]
        for wheel in wheels:
            wheel = wheel % 26
        self.fast_wheel = wheels[0]
        self.medium_wheel = wheels[1]
        self.slow_wheel = wheels[2]
        self.reverse_wheel = [letter for letter in reversed(self.alphabet)]
        
    def permutate(self, wheel):
        """
        Method to re-order the alphabet depending on the wheels settings
        
        Params:
            wheel: int
        """
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(wheel):
            new_alphabet.insert(0, new_alphabet[-1])
            new_alphabet.pop(-1)
        return new_alphabet
        
    def inverse_permutation(self, wheel):
        """
        Method to inverse re-order the alphabet depending on the wheels settings
        
        Params:
            wheel: int
        """
        new_alphabet = ''.join(self.alphabet)
        new_alphabet = list(new_alphabet)
        for iter in range(wheel):
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
            # handle empty space to ignore wheel algorithm
            if letter == ' ':
                cipher_text.append(' ')
            else:
                # letter is ciphered by fast wheel
                temp_letter = self.permutate(self.fast_wheel)[self.alphabet.index(letter)]
                # letter is ciphered by medium wheel
                temp_letter = self.permutate(self.medium_wheel)[self.alphabet.index(temp_letter)]
                # letter is ciphered by slow wheel
                temp_letter = self.permutate(self.slow_wheel)[self.alphabet.index(temp_letter)]
                # reverse_wheel is returning the inverse of that letter
                temp_letter = self.reverse_wheel[self.alphabet.index(temp_letter)]
                # letter is ciphered by slow wheel, inverse algorithm
                temp_letter = self.inverse_permutation(self.slow_wheel)[self.alphabet.index(temp_letter)]
                # letter is ciphered by medium wheel, inverse algorithm
                temp_letter = self.inverse_permutation(self.medium_wheel)[self.alphabet.index(temp_letter)]
                # letter is ciphered by fast wheel, inverse algorithm
                temp_letter = self.inverse_permutation(self.fast_wheel)[self.alphabet.index(temp_letter)]
                # append temp letter to cipher text
                cipher_text.append(temp_letter)
            # wheel rotation algorithm
            self.fast_wheel += 1
            if self.fast_wheel % len(self.alphabet) == 0:
                self.medium_wheel += 1
                self.fast_wheel = 0
            if self.medium_wheel % len(self.alphabet) == 0 and self.fast_wheel % len(self.alphabet) != 0 and self.medium_wheel >= len(
                    self.alphabet) - 1:
                self.slow_wheel += 1
                self.medium_wheel = 1
        upper_cipher_text = '' 
        for letter in cipher_text: 
            upper_cipher_text += letter  
        return ''.join(upper_cipher_text.upper())


while True:
    try:
        fast_wheel = int(input('FAST WHEEL: '))
        if fast_wheel < 1 or fast_wheel > 26:
            print('Please enter a value from 1 to 26...')
            break
        medium_wheel = int(input('MEDIUM WHEEL: '))
        if medium_wheel < 1 or medium_wheel > 26:
            print('Please enter a value from 1 to 26...')
            break
        slow_wheel = int(input('SLOW WHEEL: '))
        if slow_wheel < 1 or slow_wheel > 26:
            print('Please enter a value from 1 to 26...')
            break
        micro_cipher = MicroCipher(fast_wheel, medium_wheel, slow_wheel)
        cipher = input('CIPHER: ')
        if not cipher.isupper():
            print('Please enter only capital letters...')
            break
        print('CIPHER: ', end='')
        print(micro_cipher.cipher(cipher))
    except ValueError:
        print('Please enter a value from 1 to 26...')
        break
