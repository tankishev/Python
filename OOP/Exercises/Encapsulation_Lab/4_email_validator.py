# Create a class called EmailValidator. Upon initialization, it should receive:
# •	min_length (of the username; example: in "peter@gmail.com" "peter" is the username)
# •	mails (list of the valid mails; example: "gmail", "abv")
# •	domains (list of valid domains; example: "com", "net")
# Create three methods which should not be accessed outside the class:
# •	is_name_valid(name) - returns whether the name is greater than or equal to the min_length (True/False)
# •	is_mail_valid(mail) - returns whether the mail is in the possible mails list (True/False)
# •	is_domain_valid(domain) - returns whether the domain is in the possible domains list (True/False)
# Create one public method:
# -	validate(email) - using the three methods returns whether the email is valid (True/False)


class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        name, mail = email.split('@')
        mail, domain = mail.split('.')

        return self.__is_mail_valid(mail) and self.__is_name_valid(name) and self.__is_domain_valid(domain)
