

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)
def reverse(s):
    if len(s) <=1:
        return s
    return reverse(s[1:]) + s[0]

def isPalindrome(text):
    if len(text)<=1:
        return True
    if text[0] != text[-1]:
        return False
    return isPalindrome(text[1:-1])

def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    num = int(input("What number do you want to check? "))
    result = factorial(num)
    print(f"Factorial result of {num} is {result}")
    fib_result= fib(num)
    print (f"Fibonacci result for {num} is {fib_result}")
    # reverse_string= reverse("level")
    # print (reverse_string)
    # text_to_test= "asdfghjkllkjhgfdsa"
    # result= isPalindrome(text_to_test)
    # print(f'Is {text_to_test} reversible? {result}')


main()