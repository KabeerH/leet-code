class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #placeholder for test value
        stored_value = x
        #to reverse the number
        number = x
        reversed_number = 0

        #a reversed negative value will always result in a false
        if stored_value < 0:
            return False

        #perform reverse of test case
        while number != 0:
            digit = number % 10
            reversed_number = reversed_number * 10 + digit
            number //= 10

        #conditional checks to see if the test input case is equal to a palindrome value
        if (stored_value == reversed_number):
            return True
        else:
            return False