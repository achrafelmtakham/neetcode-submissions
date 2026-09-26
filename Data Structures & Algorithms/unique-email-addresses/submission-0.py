class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            if emails[i].count("@") == 0:
                emails[i] = ""
            else:
                local_name, domain_name = tuple(emails[i].split("@"))
                if domain_name.count(".") < 1 or len(domain_name) == 0:
                    emails[i] = ""
                else:
                    if "." in local_name:
                        local_name = local_name.replace(".", "")
                    if "+" in local_name:
                        local_name = local_name[:local_name.index("+")]
                    emails[i] = local_name + "@" + domain_name
        forward_email = {}
        for email in emails:
            forward_email[email] = forward_email.get(email, 1)
        return sum(forward_email.values())
