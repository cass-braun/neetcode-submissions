class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        s, e = 0, len(people)-1
        count = 0

        while s <= e:
            if s== e:
                count += 1
                break
            p1, p2 = people[s], people[e]
            print(s, ' ', e)
            print(p1, ' ', p2)
            print()
            if p1 + p2 <= limit:
                count += 1
                s+= 1
                e-= 1
            else:
                count += 1
                e -= 1
        return count