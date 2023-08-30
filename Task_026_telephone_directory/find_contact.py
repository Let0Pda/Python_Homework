def find_contact(word, data):

    return [item for item in data if word in item] if len(data) != 0 else None
