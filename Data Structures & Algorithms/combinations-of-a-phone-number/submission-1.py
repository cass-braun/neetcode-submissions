class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        d = {
            '2': ['a','b', 'c'],
            '3': ['d','e','f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }


        res = []

        def create(i, comb):
            if i == len(digits):
                res.append(''.join(comb))
                return

            char = digits[i]
            potential_values = d[char]

            for p in potential_values:
                comb.append(p)
                create(i+1, comb)

                comb.pop()
        
        create(0, [])

        return res