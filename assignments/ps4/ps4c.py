# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    # Example:
    # >>> is_word(word_list, 'bat') returns
    # True
    # >>> is_word(word_list, 'asdf') returns
    # False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):  # 明文->密文
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
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
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        vowels_lower = VOWELS_LOWER
        vowels_upper = VOWELS_UPPER

        dict = {}
        for i in range(len(vowels_lower)):
            dict[vowels_lower[i]] = vowels_permutation[i]
            dict[vowels_upper[i]] = vowels_permutation[i].upper()

        return dict  # 创建明文密文对应字典，此处仅考虑元音的变化
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        # 传入的是构建好的transpose_dict，直接用
        text = self.get_message_text()
        encrypted_text = ''
        for char in text:
            if char in VOWELS_LOWER + VOWELS_UPPER:
                encrypted_text += transpose_dict[char]  # 是元音的话，在transpose_dict里获取对应的密文
            else:
                encrypted_text += char  # 辅音和非字母符号不改变
        return encrypted_text  # 返回加密后的消息
        
class EncryptedSubMessage(SubMessage):  # 密文->明文
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (perm.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        max_real_words = 0
        best_permutation = ''
        best_decrypted_message = ''
        permutations = get_permutations(VOWELS_LOWER)  # 获取所有元音的排列组合
        for perm in permutations:  # 遍历每一种排列组合情况
            transpose_dict = self.build_transpose_dict(perm)  # 使用当前的permutations值构建移位字典
            decrypted_message = self.apply_transpose(transpose_dict)  # 使用当前的permutations值进行解密
            words = decrypted_message.split(' ')  # 将解密后的消息分割成单词
            real_word_count = 0
            for word in words:
                if is_word(self.get_valid_words(), word):
                    real_word_count += 1  # 计算每个猜测的permutations值对应的有效单词数量
            if real_word_count > max_real_words:
                max_real_words = real_word_count
                best_permutation = perm
                best_decrypted_message = decrypted_message  # 记录最佳的permutations值对应的解密消息
        if max_real_words > 0:
            return best_decrypted_message
        else:
            return self.get_message_text()  # 如果没有找到有效的解密结果，返回原始消息

    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")  # 创建一个SubMessage对象
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)  # 使用自定义的permutation构建字典
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))  # 查看加密后的消息

    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))  # 同样是加密后的消息
    print("Decrypted message:", enc_message.decrypt_message())  # 对加密消息进行解密
    print("----------------")
    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage("something wrong")  # 创建一个SubMessage对象
    permutation = "oauie"
    enc_dict = message.build_transpose_dict(permutation)  # 使用自定义的permutation构建字典
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "simathung wring")
    print("Actual encryption:", message.apply_transpose(enc_dict))  # 查看加密后的消息

    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))  # 同样是加密后的消息
    print("Decrypted message:", enc_message.decrypt_message())  # 对加密消息进行解密
    print("----------------")