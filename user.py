class User:
    
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        
    def check_password(self, password):
        return self.password == password
    def __str__(self):
        return f"{self.name , self.id}"
    

class Admin(User):
    def manage(self):
        print("je suis administrateur")
        return self

class Superadmin(Admin):
    def manage(self):
        print("je suis un super administrateur")
        return self
    
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
print(f"Verif user3 = {user3.manage()}")'''
etablissement = 'Lycée NDLP'
service = 'Service Informatique'
liste_divers= [etablissement, service, user1, user2, user3]

for item in liste_divers:
    print(item)