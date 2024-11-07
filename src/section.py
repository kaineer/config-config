from .serialize import serialize

def title(value):
    if type(value) == str:
        if "." in value:
            return f"[\"{value}\"]\n"
        return f"[{value}]\n"
    return ''

def section(object):
    name = title(None)
    if 'name' in object:
        name = title(object['name'])
    content = ""
    for key in object.keys():
        if key != 'name':
            content += f"{key} = {serialize(object[key])}\n"

    return name + content
