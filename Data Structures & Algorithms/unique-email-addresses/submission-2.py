class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        res = set()

        for email in emails :
            local_name,domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = ''.join(local_name.split('.'))
            res.add(local_name+domain_name)
        
        return len(res)


        