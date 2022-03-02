class User:
    
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        
    def check_password(self, password):
        return self.password == password
    

class Admin(User):
    def manage(self):
        print("je suis administrateur")
        return self

class Superadmin(Admin):
    def manage(self):
        print("je suis un super administrateur")
        return self
    
john = User()
jean = Admin()
bob = Superadmin()
john.id = 1
john.name = 'John'
john.password = '12345'
jean.id = 2
jean.name = 'Jean'
jean.password = '1234'
bob.id = 3
bob.name = 'Bob'
bob.password = '123'

print((f'Bonjour, je suis {john.name}.'))
print((f'Mon id est {john.id}.'))
print((f'Mon mot de passe est {john.password}.'))
testpassword1= input('entrez un mot de passe')
testpassword2= input('entrez un autre mot de passe')
print(f'Verification du mot de passe "1234" = {john.check_password(testpassword1)}')
print(f'Vérification du mot de passe "12345" = {john.check_password(testpassword2)}')


print(f"Verif jean = {jean.manage()}")
print(f"Verif bob = {bob.manage()}")