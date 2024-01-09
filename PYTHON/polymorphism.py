#polymorphism : means many form of same methods and they behave differently in different classes ( method overriding)


class Birds:
    def intro(self):
        print('there are many types of birds')
        
    def fly(self):
        print('many of the birds can fly but some can not fly')
        
        
class Parrot(Birds):
    def intro(self):
        print('parrot can fly')
        
        
class Penguin(Birds):
    def intro(self):
        print('penguin can not fly')
        
obj_bird=Birds()
obj_bird.intro()
obj_bird.fly()

obj_parrot = Parrot()
obj_parrot.intro()

obj_peng=Penguin()
obj_peng.intro()

