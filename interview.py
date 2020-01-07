# How to see if a word is a palindrome
def isPalindrome(word):
    word_is_palindrome = True

    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            word_is_palindrome = False
    return word_is_palindrome

print(isPalindrome("tacocat"))
print(isPalindrome("tacocats"))
print(isPalindrome(""))
print(isPalindrome("a"))
print(isPalindrome("aa"))
print(isPalindrome("abb"))


# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:
        mid = l + (r - l) / 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
            # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1
