''' Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.'''

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pontu = [',', '.', '!', '?', ';', "'"]
        for p in pontu:
            paragraph = paragraph.replace(p, " ")
        
        parag = paragraph.split()
        
        counter = {}
        for word in parag:
            word = word.lower().strip()
            if word not in banned:
                if word not in counter.keys():
                    counter[word] = 1
                else:
                    counter[word] += 1
        maxFreq = 0
        result = None
        for key in counter.keys():
            if counter[key] > maxFreq:
                maxFreq = counter[key]
                result = key
        
        return result

'''
Time complexity: O(n²)
'''