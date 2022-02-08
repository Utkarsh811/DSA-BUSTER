# Inheritance in the python
# Suppose you want to create a program for the computers .
# Supposed? now if we think about creating we have to create lotes classes for that as Coomputer is not only your Desktop
# we have servers, Digital, Hybrid , Mainframes,Analogue
# But all these types are derived from the Computers.
 # Inheritance concept is all about Parent -children relatioonship 
 # A child have all the qualities of their parents  plus they  have their own special qualities





class Animals:



    def __init__(self,legs):
        self.no_legs=legs
    
    def count(self):
        a='you belong to dog'
        b='you belong to human'
        c='you are an alien'
        if(self.no_legs==4):
            
            return a
        if(self.no_legs==2):
            return b
           
        else:
            return c
    

class Human(Animals):
    

    def __init__(self, eyes):
        self.no_eyes=eyes
    

    def recognition(self):
        ad='No doubt you are human'
        if( self.no_eyes==2):
            return ad

        
jared=Human(2)
print(jared.recognition())