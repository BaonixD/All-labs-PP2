class getString_printString:
    def __init__(self):
         self.string = ""
         
    def getString(self):
        self.string = input("enter text: ")
        
    def printString(self):
        print( self.string.upper() )
        
obj = getString_printString()
obj.getString()
obj.printString()


