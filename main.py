class CustomException(Exception):
    def __init__(self, message):
        self.message = message


try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print(f"Error: {e.message}")
