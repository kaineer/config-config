def value(_value):
    def fn():
        return _value
    return fn
