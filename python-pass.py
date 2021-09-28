

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        m_len = 0
        m_word = ""
        for first in range(len(s)):
            for second in range(first+1, len(s)+1):
                word = s[first:second]
                if (word == word[::-1]):
                    if m_len < len(word):
                        m_len = len(word)
                        m_word = word
                        
        return m_word
        
