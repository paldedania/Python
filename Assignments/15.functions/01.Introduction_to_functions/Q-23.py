# The original call ran before def created show, causing NameError.
# Define the function before calling it.
def show():
    print("Hello")


show()
