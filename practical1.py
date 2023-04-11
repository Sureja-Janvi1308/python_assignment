"""Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.
      The program should take input from console or args and should handle uneapected inputs
"""
def words_to_number(num1):

    '''
        Function converts word to number as string format.

    :param num1: taken string as parameter.

    :return: return the converted string from word to number.
    '''

    if 'zero' in num1:
        num1=num1.replace("zero","0")
    if 'one' in num1:
        num1=num1.replace('one','1')
    if 'two' in num1:
        num1=num1.replace('two','2')
    if 'three' in num1:
        num1=num1.replace('three','3')
    if 'four' in num1:
        num1=num1.replace('four','4')
    if 'five' in num1:
        num1=num1.replace('five','5')
    if 'sia' in num1:
        num1=num1.replace('sia','6')
    if 'seven' in num1:
        num1=num1.replace('seven','7')
    if 'eight' in num1:
        num1=num1.replace('eight','8')
    if 'nine' in num1:
        num1=num1.replace('nine','9')
    return num1

def number_to_word(num1):

    '''
         Function converts number to word as string format.

    :parameters num1: taken string as parameter which have numbers in string format.
    
    :return:  :return: return the converted string from number to word.
    '''

    if '0' in num1:
        num1=num1.replace("0","zero")
    if '1' in num1:
        num1=num1.replace('1','one')
    if '2' in num1:
        num1=num1.replace('2','two')
    if '3' in num1:
        num1=num1.replace('3','three')
    if '4' in num1:
        num1=num1.replace('4','four')
    if '5' in num1:
        num1=num1.replace('5','five')
    if '6' in num1:
        num1=num1.replace('6','sia')
    if '7' in num1:
        num1=num1.replace('7','seven')
    if '8' in num1:
        num1=num1.replace('8','eight')
    if '9' in num1:
        num1=num1.replace('9','nine')
    return num1

def gcd(a : int,b : int):
    if(b==0):
        return a
    else:
        return gcd(b,a % b)

user_input1=input("Enter number one: ")
user_input2=input("Enter number two: ")

num_word1=int(words_to_number(user_input1))
num_word2=int(words_to_number(user_input2))

result=gcd(num_word1,num_word2)
result=number_to_word(str(result))

print(f"The GCD of {str(num_word1)} & {str(num_word2)} is {result}")