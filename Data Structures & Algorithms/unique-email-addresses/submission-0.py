class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsDict = {}
        numEmails = 0
        for email in emails:
            local = email.split('@')[0]

            local = ''.join(local.split('.'))

            local = local.split('+')[0]

            newEmail = local + '@' + email.split('@')[1]
            print(newEmail)
            if newEmail not in emailsDict:
                numEmails +=1
                emailsDict[newEmail] = True
        
        return numEmails