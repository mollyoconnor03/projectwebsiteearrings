from model.User import User


class UserDAO:
    def __init__(self):
        self.users = [
            User(1, "John@gmail.com", "pw1", True),
            User(2, "Jane@gmail.com", "pw2", False)]

    def get_all_users(self):
        return self.users

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
