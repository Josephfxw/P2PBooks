import os
from database.database_objects import serialize_user, User

USER_LIST = ["Chris",
             "MD",
             "Porrith",
             "Fioger"]

EMAIL_LIST = ["chris@gmail.com",
              "md@gmail.com",
              "porrith@gmail.com",
              "fioger@gmail.com"]

DOB_LIST = ["1/26/1995",
            "1/1/1993",
            "7/17/1995",
            "12/26/1995"]

for i in range(4):
    serialize_user(User(username=USER_LIST[i],
                        password="pw",
                        email=EMAIL_LIST[i],
                        dob=DOB_LIST[i],
                        group_policy='SU',
                        ), USER_LIST[i])

