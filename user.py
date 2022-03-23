from abc import abstractmethod


class Profile:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
    @abstractmethod
    def get_profile(self):
        pass

class User(Profile):
    _age = 0

    
    @property
    def age(self):
        return self._age
    
    @age.setter
    
    def age(self,new_age):
        if new_age > 0 and new_age <120:
            self._age = new_age
        else:
            print("veuillez renseigner un âge valide")
    
    def check_password(self, password):
        return self.password == password
    def __str__(self):
        return f"{self.name , self.id}"
    def get_profile(self):
        return "User"


class Admin(User):
    def manage(self):
        print("je suis administrateur")
        return self
    def get_profile(self):
        return "Admin"

class Superadmin(Admin):
    def manage(self):
        print("je suis un super administrateur")
        return self
    def get_profile(self):
        return "Superadmin"

user1 = User(1,'John','12345')
user2 = Admin(2,'John', '1234')
user3 = Superadmin(3, 'Bob', '123')


'''print((f'Bonjour, je suis {user2.name}.'))
print((f'Mon id est {user2.id}.'))
print((f'Mon mot de passe est {user2.password}.'))
testpassword1= input('entrez un mot de passe')
testpassword2= input('entrez un autre mot de passe')
print(f'Verification du mot de passe "1234" = {user2.check_password(testpassword1)}')
print(f'Vérification du mot de passe "12345" = {user2.check_password(testpassword2)}')


print(f"Verif user1 = {user1.manage()}")
print(f"Verif user3 = {user3.manage()}")
etablissement = 'Lycée NDLP'
service = 'Service Informatique'
liste_divers= [etablissement, service, user1, user2, user3]

for item in liste_divers:
    print(item)
user1.age = int(input('veuillez renseigner un age : '))
print(f'{user1.name} a {user1.age} ans')'''
users = [user1,user2,user3]
for user in users:
    print(f"{user.name} est {user.get_profile()}")
