class employee:
    def __init__(self):
        print("Employee is created")
    def __del__(self):
        print("Destructor is called")
def create_obj():
    print("Making Object...")
    obj = employee()
    print("function ends...")
    return obj

print("Calling create_obj()...")
obj = create_obj()
print("program ends...")
