class UserAlreadyExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class DataNotFoundError(Exception):
    pass

class InvalidEnteredDataError(Exception):
    pass

class NotEnoughRights(Exception):
    pass