""" 
    Class:  User
"""

#regualr imports
import datetime
import uuid



#user class
class User(object):

    def __init__(self, user_name, first_name, last_name, 
                 email, contact_number, 
                 password, 
                 active_user, is_active, 
                 gender, date_of_birth, user_type, 
                 available_for_boarding, address, 
                 date_joined,  _id=None):


        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact_number = contact_number
        self.password = password
        self.active_user = active_user
        self.is_active = is_active
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.user_type = user_type
        self.available_for_boarding = available_for_boarding
        self.address = address
        self.date_joined = date_joined
        self._id = uuid.uuid4().hex if _id is None else _id

     
   
