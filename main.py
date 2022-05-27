class Student:
  def __init__(self, _name, _age, _track, _score):
     self.name = _name
     self.age = _age
     self.track = _track
     self.score = _score

  def change_name(self, _name):
      self.name =  _name
  def change_age(self, _age):
      self.age = _age 
  def add_track(self, _track):
        self.track = _track
  def get_score(self):
        return self.score
p1 = Student("John", 36, "fullstack", 80.3)

print(p1.name)
print(p1.age)
print(p1.track)
print(p1.score)

Student.change_name(p1, "Peter")
print(p1.name)

Student.change_age(p1, 34)
print(p1.age)

Student.add_track(p1, "UI/UX")
print(p1.track)

Student.get_score(p1)
print(p1.score)