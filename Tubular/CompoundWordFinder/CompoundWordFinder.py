#Created by Mina Habib
import sys
import solution

if __name__=='__main__':
    uniqueSet = set()
    for line in sys.stdin:
        tmp = line.rstrip()
        tmp = tmp.strip()
        uniqueSet.add(tmp)
    uniqueList = list(uniqueSet) 
    uniqueList.sort(key=len)
    getWords = solution.solution()
    getWords.CompoundWordFinder(uniqueList)
    getWords.result.sort()
    for i in getWords.result:
        sys.stdout.write(str(i) +  '\n')