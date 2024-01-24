# # class person:
# #     blood_color = 'red'
# #     def __init__(self,name):
# #          self.name = name
# #     def singing(self):
# #          return f'{self.name}가 노래함'

# # singer = person('iu')
# # print(singer.singing())
# # print(singer.blood_color)
# # print(singer.name)

# class person:
#     name = 'unknown'
#     def talk(self):
#         print(self.name)

# p1 = person()
# p1.talk()   # unknown

# p2 = person()
# p2.name ='sinijini'
# p2.talk()   # sinijini

# p2.ssafy = 11
# print(p2.ssafy) # 11


# class Circle():
#     pi = 3.14
#     def __init__(self,r) :
#         self.r = r

# print(Circle.pi)

# c1 = Circle(2)
# c2 = Circle(2)
# c2.pi = 5
# print(c1.pi)
# print(c2.pi)

class Person:
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1
    @classmethod
    def num_person(cls):
        print(cls)
        print(f'인구수는 {cls.count}')

p1 =Person ('iu')
p2 = Person('bts')
Person.num_person()