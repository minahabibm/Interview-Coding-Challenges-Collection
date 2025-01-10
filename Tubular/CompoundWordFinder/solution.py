#Created by Mina Habib
from collections import Counter
import re

class solution:

  def __init__(self):
    self.result = []

  def checkSequence(self, word, seen):
    def findOccurrences(substring):
      matches = re.finditer(substring, word)
      matches_positions = [[match.start(), match.end()] for match in matches]
      return matches_positions
    def checkArr(start, end):
      for i in range(start,end): 
        if wordArr[i]:
          return False 
      return True
    def addToWordArray(startIndex, endIndex, wordStr ):
      if checkArr(startIndex, endIndex):
        wordItr = 0
        for j in range(startIndex, endIndex):
          wordArr[j] = wordStr[wordItr]
          wordItr += 1
      return True
  
    n = len(word)
    wordArr = [ "" for i in range(n)]
    seenArr = list(seen)
    seenArr.sort(key= len, reverse= True)
    for i in seenArr:
      Occurrences = findOccurrences(i)
      for x, y in Occurrences:
        if checkArr(x, y):
          if addToWordArray(x, y, i): break    
    if "" in wordArr:
      return False
    return True
  
  def getValidformWord(self, word, arrays):
    def backtracking(A):
      sumOfEle = sum(len(x) for x in A)
      if sumOfEle < y:
        return
      if sumOfEle == y:
        res.add(tuple(A))
        return
      n = len(A)
      for i in range(n):
        tmp = A[:]
        tmp.pop(i)
        backtracking(tmp)
    
    res = set()
    y = len(word)
    arr = []
    backtracking(list(arrays))
    for i in res : 
      if self.checkSequence(word, i):
        return True
    return False

  def formWord(self, word, wordDict):
    if not word or len(word) == 0: return False
    seen = set()
    for i in wordDict:
      if i in word: seen.add(i)
    return self.getValidformWord(word , seen)

  def CompoundWordFinder(self, wordDict):
    if not wordDict or len(wordDict) == 0:
      return []
    preWords = set()
    self.result = []
    for word in wordDict: 
      if self.formWord(word, preWords):
        self.result.append(word)
      preWords.add(word)
    self.result.sort()          
    return self.result
