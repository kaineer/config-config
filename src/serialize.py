def serialize_number(value):
    return str(value)

def serialize_boolean(value):
    if value:
        return 'true'
    return 'false'

def serialize_string(value):
    decoded = value.encode('latin1').decode('utf8')
    return f"\"{decoded}\""

def serialize_list(value):
    items = (serialize(x) for x in value)
    content = ", ".join(items)
    return f"[{content}]"

def serialize(value):
    if type(value) == int:
        return serialize_number(value)
    if type(value) == bool:
        return serialize_boolean(value)
    if type(value) == str:
        return serialize_string(value)
    if type(value) == list:
        return serialize_list(value)

__all__ = ["serialize"]
