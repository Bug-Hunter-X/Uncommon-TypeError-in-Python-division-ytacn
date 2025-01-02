def function_with_uncommon_error(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if b == 0:
                print("Error: Division by zero")
                return None
            result = a / b
            return result
        else:
            print("Error: Unsupported operand type(s) for / ")
            return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

#Corrected code
result = function_with_uncommon_error(10, 2) #Valid Input
print(result)
result = function_with_uncommon_error("hello", 2) #Invalid Input
print(result)
result = function_with_uncommon_error(10, 0) #Division by Zero
print(result)