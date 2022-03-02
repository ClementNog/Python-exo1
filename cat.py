class Cat:
    pass
    def grow(self):
        nbrtaille = int(input('de quelle taille a grandi le chat '+ self.name + ' '))
        self.size += nbrtaille
        return self.name, self.size
    def showcolor(self):
        return self.name, self.color


chat1 = Cat()
chat1.name = 'Minou'
chat1.size = 23
chat2 = Cat()
chat2.name = 'Kitty'
chat2.size = 17
chat1.color = 'blue'
chat2.color = 'black'
print(f"Voici les anciennes tailles de {chat1.name , chat1.size} et de {chat2.name , chat2.size} et maintenant voici leur taillle actuel {chat1.grow()} et {chat2.grow()}")
if chat2.size > chat1.size:
    print('cheh !')
print(f"{chat1.showcolor() , chat2.showcolor()}")