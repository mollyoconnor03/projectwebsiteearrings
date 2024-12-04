from dao.UserDAO import UserDAO


class UserService:
    def __init__(self):
        self.userDAO = UserDAO()

    def get_all_users(self):
        return self.userDao.get_all_users()

    def get_user_by_email(self, email):
        return self.userDAO.get_user_by_email(email)
