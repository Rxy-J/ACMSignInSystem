from main.utils.DAO.DAO import DAOForUser
from main.utils.ACM.ACM import ACMUser

t = {'username': '2019300089', 'password': 'asdf', 'name': 'a', 'email': '742363155@qq.com', 'joinTime': '2021-10-08', 'emailVerify': 'de42', 'adminVerify': '', "admin": False}
user = DAOForUser.getUserByUsername("admin")
print(user)
# DAOForUser.addUser(user)
print(user.getDict())
# print()