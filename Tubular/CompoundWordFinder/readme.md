# Compound Word Finder

## Solution Discussion
Compound Word Finder challenge requires to find if a word in the array can be made up by other words inside that array, here we can find the solution using DP or BFS or a Trie data Structure, which lead us to a simple solution like that, 

```python
  # After Sorting the Array, and iterating on each word inside the array up to its size we run this function to check if this word can be formed.

 def formWord(self, s, wordDict):
   if not wordDict: return False
   n = len(s)
   dp = [False for i in range(n+1)]
   dp[0] = True
   for i in range(n + 1):
     for j in range(i):
       if dp[j] and s[j:i] in wordDict:
         dp[i] = True
         break
   return dp[len(s)]
``` 

but here in this coding challenge we have a few more constraints, needed to be aware of, which A component word can only be used once when forming a compound word. 

on that note we can start to work on actual solution, using the above solution with any other combination of solutions wont be sufficient, as by observing above function this code sample case would fail.

```
[car,race,racecar, racecarracecar]
the above function will result into [racecar, racecarracecar]
that is the correct answer, if we are using repeated words, which in this case we dont allow.
The dp array would check and find the second racecar again and stops.
i needed something more to avoid using the word racecar twice and use race, car, racecar -> racecarracecar
```  
which led to sort the words Array input in ascending order and use all the words inside the Array leading up to the compound word based on the fact no compound word would be made of another word of the same size. and check if they exist in the compound word. if they do, we can add up all these words in a set() to prevent duplicates, and then we can further investigate if all words in this set makes up the compound word or not.

to decide if these words can make a compound word or not, we need to count all the chars in this set and compare to the compound word chars count, this leads to three possibilities, counter for the set bigger than, equal, or less than the counter for compound word.

if the counter for the set has any char less than the char count int the counter for the compound word, we can safely eliminate this word as it cannot be formed by the words in the Array.
Equals or more than for each char in the counter for the compound, if all chars in the set counter equals to the char in the compound counter, one can assume that; return this word as valid, not in this case,
```
[woman, manwo, womanwoman]
both words [woman, manwo] exist in [womanwoman] and both [woman, manwo] have the same count for each char in [womanwoman]. notice that cant form a word womanwoman not with the challenge constraints.
```
so we treat bigger or equal counts the same, and we can decide if they form a valid Compound word or not if somehow constructed an array of compound word length, and fill it with words from the set. if they form the compound word then return that word as a valid, if any char is missing then it is not valid. we are allowed to do so because bigger words exist in the set has higher priority, where smaller words, can lastly fill the blanks.

## Time and Space Complexity
### Time Complexity
* O(nlogn + N^2 * M) for best case
* O(nlogn + N^2 * ( (M^2 + W^2 + D) + (M*(W+Y)*Y))for worst case
  * N -> length of Words Array, 
  * M -> length of seen, 
  * W -> length of word, 
  * D -> length of Counter for word, 
  * Y -> length of for matches
  * nlogn -> sorting algorithm
  
### Space Complexity
* O((preword +  uinqueqords) * (sumOfSeen + couWords + couSeen) for best case
* O((preword +  uinqueqords) * (sumOfSeen + couWords + couSeen) * (matches_positions + wordArr)) for worst case

# Notes
* Python 3.9.4
* since i cant manipulate the answer file directly, and diff would compare my answer vs answer.txt, please make sure answer.txt has a new line at the end of file. 

