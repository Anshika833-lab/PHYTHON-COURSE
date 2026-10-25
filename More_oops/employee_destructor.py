class employee:

    def __init__(self):
        print("employee created")

    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making Object...")
    obj = employee()
    print("function end...")
    return obj


print("Calling create_obj() function...")
obj = create_obj()
print("program End...")

