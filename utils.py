def validate(func):
    def decorated():
        print("validate")
        func()
    return decorated