class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsDict = {}
        numEmails = 0
        for email in emails:
            local, domain = email.split('@')

            local = ''.join(local.split('.'))

            local = local.split('+')[0]

            newEmail = local + '@' + domain

            if newEmail not in emailsDict:
                numEmails +=1
                emailsDict[newEmail] = True
        
        return numEmails