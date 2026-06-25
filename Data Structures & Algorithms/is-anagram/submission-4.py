class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMap1 = {}        
        hashMap2 = {} 

        if len(s) == len(t):
            for char in s:
                if char in hashMap1:
                    hashMap1[char] = hashMap1[char] + 1
                else:
                    hashMap1[char] = 1  

            for char in t:
                if char in hashMap2:
                    hashMap2[char] = hashMap2[char] + 1
                else:
                    hashMap2[char] = 1    



            for char, count in hashMap1.items():
                if char not in  hashMap2 or count != hashMap2[char]:
                    return False

            return True
        else:
            return False    
         