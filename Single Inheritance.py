class Cricket:
    @staticmethod
    def T20():
        print("This is 20 Over formate of cricket.")
    
    @ staticmethod
    def ODI():
        print("This is 50 over formate of cricket.")
        
    @ staticmethod
    def Test():
        print("It is the unlimate over formate lasts for 5 days.")
        
class IPL(Cricket):
    def __init__(self,name):
        self.name = name
        
Cric1 = Cricket("CSK")

print(Cric1.Test)