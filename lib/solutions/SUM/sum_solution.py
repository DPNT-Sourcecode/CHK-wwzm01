# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x >= 0 and x <= 100 and y >= 0 and y <= 100: #make sure integers fall within the parameters
        result = x + y #sum the integers
        return result #return the result
    else:
        return "One or both integers did not fall within the parameters" #return error message


