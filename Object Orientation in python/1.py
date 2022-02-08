#when workinig with objects variables are called attriburtes and functions are called methods
class Triangle:

    def area(self): # method , you must be wondering function defination have no arguments and functiion  callin too.Well.
        areas= self.side1*self.side2*self.side3
        return areas
    
# creating object
triangle1=Triangle()
triangle1.side1=3
triangle1.side2=4
triangle1.side3=6

print(triangle1.side1)
print(triangle1.side2)
print(triangle1.side3)


print(triangle1.area())


#python has __iinit__ method for defining the element


class Student:

    def pass_fail(self):
        a="The marks entered are incorrect"
        if(self.marks1 +self.marks2>=140):
            return True
        elif(self.marks1+ self.marks2 >200 and self.marks1+ self.marks2<0):
            return a


        else:
            return False
        
    def __init__(self,marks1,marks2):
        self.marks1=marks1
        self.marks2=marks2


jared=Student(56,87)
mridula=Student(30,30)

print(jared.pass_fail())
print(mridula.pass_fail())



#Everything is an object in python
nums1=[1,2,3]
print(type(nums1))   #<class 'list'> # nums1 is an object of class list
nums=dict()
print(type(nums))    #<class 'dict'>


# dir in python
print(dir(nums1))  #['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# id in python
# every object has an id in python
nrms=[1,2,3,4,5]
print(id(nrms))    #2798186179456




mns=nrms
print(id(mns))    #2798186179456
 # conclusion as we can see both  mns and nrms have same id  so changes done in nrms also reflect on mns

mns=mns.__add__([53,64,746,67,'5353',63535])
print(mns)


a=9
b=a
print(id(a),id(b))  #1779933276720 1779933276720  #python do this for memory optimization
va=[2,3,5,6,7,86,5]
av=va.copy()
print(id(va),id(av))    #2724822625472 2724822625344   # using copy method both got different id
