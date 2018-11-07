class MessageNotFoundError(Exception):
    def __init__(self, message="Message ID not found!"):
        super().__init__(message)
        self.error = message


class UserNotFoundError(Exception):
    def __init__(self, message="User not found!"):
        super().__init__(message)
        self.error = message


class MismatchJobAuthorError(Exception):
    def __init__(self, username, jobid):
        self.message = f"Username {username} is not the author of Job ID {jobid}"
        super().__init__(self.message)
        self.error = self.message
