def roll_call(name, age, phone):
    print("name", name,"age",age,"phone",phone)
    
    
student1 = ['beau', 20, '0438']
student2 = {"name": "john", "age": 23, "phone": "0438"}


roll_call('beau', 20, '0438')
roll_call(*student1)
roll_call(**student2)

