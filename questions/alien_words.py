"""
Problem: Ordering of Alien Dictionary

Description:
There is a dictionary of words from an alien language. While we know the words, we do not know the ordering of the characters in this language. Given a list of words from this alien dictionary sorted lexicographically according to the rules of the alien language, deduce the correct order of characters in the alien language.

Function Signature:
def find_order(words: List[str]) -> str:

Inputs:
    - words (List[str]): A list of words from the alien dictionary sorted according to the rules of the alien language.

Returns:
    - str: The deduced order of characters in the alien language.

Examples:
1. Input: ["ba", "bc", "ac", "cab"]
   Output: "bac"
   Explanation: 
   1. From "ba" and "bc", we conclude 'a' comes before 'c'.
   2. From "bc" and "ac", we conclude 'b' comes before 'a'.
   Thus, the character order is "bac".

2. Input: ["cab", "aaa", "aab"]
   Output: "cab"
   Explanation: 
   1. From "cab" and "aaa", we conclude 'c' comes before 'a'.
   2. From "aaa" and "aab", we conclude 'a' comes before 'b'.
   Thus, the character order is "cab".

3. Input: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
   Output: "ywxz"
   Explanation:
   1. From "ywx" and "wz", we conclude 'y' comes before 'w'.
   2. From "wz" and "xww", we conclude 'w' comes before 'x'.
   3. From "xww" and "xz", we conclude 'w' comes before 'z'.
   4. From "xz" and "zyy", we conclude 'x' comes before 'z'.
   5. From "zyy" and "zwz", we conclude 'y' comes before 'w'.
   Thus, the character order is "ywxz".

Notes:
    - This problem can be approached by building a directed graph where each character is a node and edges represent the order between characters.
    - After the graph is built, a topological sort can be performed on the graph to determine the order of characters.
    - A key step in this process is to compare adjacent words in the given list and establish character order based on their differences.

Tags:
    - Graphs
    - Topological Sorting
"""
from typing import List

def find_order(words: List[str]) -> str:
  return ""