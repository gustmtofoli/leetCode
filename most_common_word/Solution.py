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