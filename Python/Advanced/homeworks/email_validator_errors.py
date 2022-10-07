class NameTooShortError(Exception):
    def __init__(
        self, name: str, message: str = "Name must be more than 4 characters",
    ) -> None:
        self.message = message
        self.name = name
        super().__init__(message)


class MustContainAtSymbolError(Exception):
    def __init__(
        self, email: str, message: str = "Email must contain @"
    ) -> None:
        self.message = message
        self.email = email
        super().__init__(message)


class InvalidDomainError(Exception):
    def __init__(
        self,
        domain: str,
        message: str = "Domain must be one of the following: .com, .bg, .org, .net",
    ) -> None:
        self.message = message
        self.domain = domain
        super().__init__(message)


data = input()
valid_domains = [".com", ".bg", ".org", ".net"]

while data != "End":
    if "@" not in data:
        raise MustContainAtSymbolError(data)
    else:
        name = data.split("@")[0]
        domain = "." + data.split("@")[1].split(".")[1]
        if len(name) <= 4:
            raise NameTooShortError(name)
        elif domain not in valid_domains:
            raise InvalidDomainError(domain)
        else:
            print("Email is valid")
    data = input()
