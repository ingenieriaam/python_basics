#############################################
# new_module components
variable = "this is a variable from new_module"

def some_function():
    print("this is a function from new_module")

class some_class:
    def __init__(self):
        print("this is a class from new_module")

#############################################
# Execution of the New_Module file itself
if __name__ == "__main__":
    print("this is new_module execution")