class Profile:
    def __init__(self, _name: str, _password: str) -> None:
        if 5 <= len(_name) <= 15:
            self.__name = _name
        else:
            raise ValueError(
                "The username must be between 5 and 15 characters."
            )
        if (
            any(x.isupper() for x in _password)
            and any(x.islower() for x in _password)
            and any(x.isdigit() for x in _password)
        ):
            self.__password = _password
        else:
            raise ValueError(
                "The password must be 8 or more characters with at "
                "least 1 digit and 1 uppercase letter."
            )

    def __str__(self) -> str:
        return (
            f'You have a profile with username: "{self.__name}" and password: '
            f'{"*" * len(self.__password)}'
        )
