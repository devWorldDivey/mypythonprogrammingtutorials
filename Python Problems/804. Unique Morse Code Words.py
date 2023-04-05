"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
"""

words = ["gin", "zen", "gig", "msg"]


class Solution:

    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        res = []

        for i in range(len(words)):
            k = ""
            for j in words[i]:
                k += self.give_morse_code(j)
            res.append(k)

        print(len(set(res)))

    def give_morse_code(self, code1) -> str:
        import string

        az_Upper = string.ascii_lowercase
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        list(enumerate(az_Upper))
        dict1 = {}
        for i in range(len(az_Upper)):
            dict1.update({az_Upper[i]: morse_code[i]})
        # print(dict1[code1])
        return dict1[code1]


my_sol = Solution()
my_sol.uniqueMorseRepresentations(words)
