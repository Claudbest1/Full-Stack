class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks, score):
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score
        trackss=",".join(self.tracks)
        print("My name is "+ self.name)
        print("My age is "+ str(self.age))
        print("My track is "+ trackss)
        print("My score is "+ str(self.score))
    #Method 1
    def change_name(self, new_name):
        self.name= new_name
        print( "My name is "+ self.name)
    #Method 2    
    def change_age(self, new_age):
        self.age= new_age
        print( "My age is "+ str(self.age)) 
    #Method 3    
    def add_track(self, new_track):
        self.tracks.append(new_track)
        str1=",".join(self.tracks)
        print( "My track is "+ str1)
     #Method 4    
    def get_score(self, score):
        self.score=score
        print("My score is "+ str(self.score))       
        
Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(95.24)
