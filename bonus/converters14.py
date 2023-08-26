def convert(feet, inches):
    try:
        meters = feet * 0.3048 + inches * 0.0254
    except TypeError:
        return "Wrong params"
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
    return meters
