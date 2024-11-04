# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # 如果所有的字母都在猜过的列表中，返回True；否则返回False
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # 如果字母在要猜的单词中，显示该字母；否则显示"_"。
    result = ""
    for i in secret_word:
        if i not in letters_guessed:
            result += "_ "
        else:
            result += i
    return result

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # 猜过的字母从可用字母列表中移除。
    available = ""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            available += i
    return available


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guessed_word = ""  # 初始化一个变量用来存储截止目前的猜测
    num_of_guesses = 6  # 猜测次数初始化为6
    num_of_warnings = 3  # 警告次数初始化为3
    available_letters = string.ascii_lowercase  # 可用字母列表初始化为所有小写字母
    letters_guessed = []  # 猜过字母的列表
    print("Welcome to the game Hangman!\nI am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", num_of_warnings, "warnings left.")

    # 猜测次数还未用完且猜测的单词还没有完全被猜出时，游戏继续进行。
    while num_of_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have", num_of_guesses, "guesses left.")
        print("Available letters:", available_letters)
        guess = input("Please guess a letter: ").lower()  # Convert to lowercase

        # 检查用户输入是否是字母
        if not guess.isalpha():
            if num_of_warnings > 0:
                num_of_warnings -= 1
                print("Oops! That is not a valid letter. You have", num_of_warnings, "warnings left:", guessed_word)
            else:
                num_of_guesses -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",
                      guessed_word)
        elif guess in letters_guessed:
            if num_of_warnings > 0:
                num_of_warnings -= 1
                print("Oops! You've already guessed that letter. You have", num_of_warnings, "warnings left:",
                      guessed_word)
            else:
                num_of_guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                      guessed_word)
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                print("Good guess:", guessed_word)
            else:
                if guess in 'aeiou':
                    num_of_guesses -= 2  # Vowels cost two guesses
                else:
                    num_of_guesses -= 1
                print("Oops! That letter is not in my word:", guessed_word)

        available_letters = get_available_letters(letters_guessed)
        print("------------------")

    # 猜测次数用完，判断是否每一个字母都猜中了
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        # 分数为剩余猜测次数*单词中唯一字母的数量
        print("Your total score for this game is:", num_of_guesses * len(set(secret_word)))
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # 去除 my_word 中的空格
    my_word = my_word.replace(' ', '')

    # 长度不相等，直接返回False
    if len(my_word) != len(other_word):
        return False

    # 已经猜到的字母集合
    revealed_letters = set()

    for i in range(len(my_word)):
        if my_word[i] == '_':
            # 如果other_word中的这个位置的字母已经在my_word中出现过，返回 False
            if other_word[i] in revealed_letters:
                return False
        else:
            # 收集已经猜到的字母
            revealed_letters.add(my_word[i])
            # 检查上面收集到字母是否匹配other_word对应位置字母
            if my_word[i] != other_word[i]:
                return False

    # 由于my_word中"_"出现的时候，可能有重复字母还未添加到revealed_letters中
    # 因此revealed_letters收集完后，再遍历other_word检查一遍
    for i in range(len(my_word)):
        if my_word[i] == '_' and other_word[i] in revealed_letters:
            return False

    return True

# print(match_with_gaps("a_ ple", "apple"))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # 遍历wordlist，如果已猜出的位置与单词匹配上了，打印出该单词。
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""  # 初始化一个变量用来存储截止目前的猜测
    num_of_guesses = 6  # 猜测次数初始化为6
    num_of_warnings = 3  # 警告次数初始化为3
    available_letters = string.ascii_lowercase  # 可用字母列表初始化为所有小写字母
    letters_guessed = []  # 猜过字母的列表
    print("Welcome to the game Hangman!\nI am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", num_of_warnings, "warnings left.")

    # 猜测次数还未用完且猜测的单词还没有完全被猜出时，游戏继续进行。
    while num_of_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have", num_of_guesses, "guesses left.")
        print("Available letters:", available_letters)
        guess = input("Please guess a letter: ").lower()  # Convert to lowercase

        # 检查用户输入是否是字母，不是字母的进行警告，*号例外
        if not guess.isalpha():
            # 新增hint功能，如果输入*，提示可能的匹配单词
            if guess == '*':
                # 传入当前已猜的部分
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:
                if num_of_warnings > 0:
                    num_of_warnings -= 1
                    print("Oops! That is not a valid letter. You have", num_of_warnings, "warnings left:", guessed_word)
                else:
                    num_of_guesses -= 1
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",
                          guessed_word)
        elif guess in letters_guessed:
            if num_of_warnings > 0:
                num_of_warnings -= 1
                print("Oops! You've already guessed that letter. You have", num_of_warnings, "warnings left:",
                      guessed_word)
            else:
                num_of_guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                      guessed_word)
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                print("Good guess:", guessed_word)
            else:
                if guess in 'aeiou':
                    num_of_guesses -= 2  # Vowels cost two guesses
                else:
                    num_of_guesses -= 1
                print("Oops! That letter is not in my word:", guessed_word)

        available_letters = get_available_letters(letters_guessed)
        print("------------------")

    # 猜测次数用完，判断是否每一个字母都猜中了
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        # 分数为剩余猜测次数*单词中唯一字母的数量
        print("Your total score for this game is:", num_of_guesses * len(set(secret_word)))
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # 从words.txt中随机选择一个单词作为秘密单词。
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    # 自定义一个单词用于测试
    # hangman("tact")

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    # hangman_with_hints("apple")
