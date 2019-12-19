class Solution:
    def numUniqueEmails(self, emails: List[str]):
        emails_hash = set()
        for i in range(len(emails)):
            email = emails[i]
            local_domain = email.split('@')
            local = local_domain[0].replace('.','')
            if '+' in local:
                local = local[:local.index('+')]
            final_email = local+ "@" + local_domain[1]
            if final_email not in emails_hash:
                emails_hash.add(final_email)
        return len(emails_hash)