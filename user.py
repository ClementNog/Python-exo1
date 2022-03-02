class User:
    pass
    def check_password(self, password):
        
        return self.password == password

john = User()

john.id = 1
john.name = 'John'
john.password = '12345'
print((f'Bonjour, je suis {john.name}.'))
print((f'Mon id est {john.id}.'))
print((f'Mon mot de passe est {john.password}.'))
testpassword1= input('entrez un mot de passe')
testpassword2= input('entrez un autre mot de passe')
print(f'Verification du mot de passe "1234" = {john.check_password(testpassword1)}')
print(f'Vérification du mot de passe "12345" = {john.check_password(testpassword2)}')
