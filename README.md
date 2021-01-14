# isValid-coding-challenge
Repository that stores the IsValid() function as part of a coding challenge

Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

**Example**

* s=abc
This is a valid string because frequencies are {a: 1, b: 1, c: 1}.


* s=abcc
This is a valid string because we can remove one c and have 1 of each character in the remaining string.

* s=abccc
This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a: 1, b: 1, c: 2}.

**Function Description**

Complete the isValid function. isValid has the following parameter(s):

* string s: a string

**Returns**
* string: either YES or NO

**Input Format**

A single string s.
