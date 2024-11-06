# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    # >>> is_word(word_list, 'bat') returns
    # True
    # >>> is_word(word_list, 'asdf') returns
    # False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()  # 创建word_list的副本并从外部访问

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = alphabet_lower.upper()
        shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
        shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]
        dict = {}
        for i in range(len(alphabet_lower)):
            dict[alphabet_lower[i]] = shifted_alphabet_lower[i]
            dict[alphabet_upper[i]] = shifted_alphabet_upper[i]
        return dict  # 创建了明文密文的对应字典

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        text = self.get_message_text()  # 原文
        shift_dict = self.build_shift_dict(shift)  # 根据传入的shift值，构建明文密文对应字典
        shifted_message = ""
        for char in text:
            if char.isalpha():
                shifted_message += shift_dict[char]  # 是字母的话，在shift_dict找到对应的密文
            else:
                shifted_message += char  # 非字母符号不改变
        return shifted_message  # 应用字典进行加密，返回加密后的消息


class PlaintextMessage(Message):  #  明文->密文
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)  # 调用父类Message的构造函数
        self.shift = shift  # 新增一个属性shift
        self.encryption_dict = self.build_shift_dict(self.shift)  # 明文密文对应字典
        self.message_text_encrypted = self.apply_shift(self.shift)  # 加密后的消息

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()  # 创建字典的副本并从外部访问

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift  # 更新shift值
        self.encryption_dict = self.build_shift_dict(self.shift)  # 基于shift值的变量也要更新
        self.message_text_encrypted = self.apply_shift(self.shift)  # 基于shift值的变量也要更新


class CiphertextMessage(Message):  # 密文->明文
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # 遍历所有可能的shift值，并计算每个shift值下解密后的消息中有效单词的数量，取最多者为最佳解密
        best_shift = 0
        max_real_words = 0
        for shift in range(26):
            decrypted_message = self.apply_shift(shift)  # 尝试每个shift值
            words = decrypted_message.split(' ')  # 将解密后的消息分割成单词
            real_word_count = 0
            for word in words:
                if is_word(self.get_valid_words(), word):
                    real_word_count += 1  # 计算每个猜测的shift值对应的有效单词数量
            if real_word_count > max_real_words:
                max_real_words = real_word_count
                best_shift = shift  # 找到最大有效单词数量对应的shift值
        return (best_shift, self.apply_shift(best_shift))  # 采用找到的shift值进行解密


if __name__ == '__main__':
    #    #Example test case (PlaintextMessage)
    #    plaintext = PlaintextMessage('hello', 2)
    #    print('Expected Output: jgnnq')
    #    print('Actual Output:', plaintext.get_message_text_encrypted())
    #
    #    #Example test case (CiphertextMessage)
    #    ciphertext = CiphertextMessage('jgnnq')
    #    print('Expected Output:', (24, 'hello'))
    #    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    test_message1 = 'hello'
    plaintext = PlaintextMessage(test_message1, 2)
    print('Input:', test_message1)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print("---------------")

    test_message2 = 'test case 2'
    plaintext = PlaintextMessage(test_message2, 5)
    print('Input:', test_message2)
    print('Expected Output: yjxy hfxj 2')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print("---------------")

    ciphertext = CiphertextMessage('jgnnq')
    print('Input: jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    print("---------------")

    #TODO: best shift value and unencrypted story
    encrypted_story = get_story_string()  # 需要解密的story.txt
    ciphertext = CiphertextMessage(encrypted_story)
    print('Actual Output:', ciphertext.decrypt_message())
