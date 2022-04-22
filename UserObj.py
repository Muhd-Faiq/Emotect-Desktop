class UserObj(object):
    def __init__(self):
        self._name = None
        self._email = None
        self._role = None

    ####name start#####
    @property
    def name(self):
        """I'm the 'name' property."""
        print("getter of name called")
        return self._name

    @name.setter
    def name(self, value):
        print("setter of name called")
        self._name = value

    @name.deleter
    def name(self):
        print("deleter of name called")
        del self._name

    ####name end#####
    
    ####email start#####
    @property
    def email(self):
        """I'm the 'email' property."""
        print("getter of email called")
        return self._email

    @email.setter
    def email(self, value):
        print("setter of email called")
        self._email = value

    @email.deleter
    def email(self):
        print("deleter of email called")
        del self._email

    ####email end#####

    ####role start#####
    @property
    def role(self):
        """I'm the 'role' property."""
        print("getter of role called")
        return self._role

    @role.setter
    def role(self, value):
        print("setter of role called")
        self._role = value

    @role.deleter
    def role(self):
        print("deleter of role called")
        del self._role

    ####role end#####

    