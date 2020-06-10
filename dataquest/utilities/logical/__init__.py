def are_unique(column):
    # creates two lists: one for keeping unique values, and
    # another for storing duplicate entries
    unique = []
    duplicate = []

    # loop through values in list
    for value in column:
        if value in unique:
            # if we found a occurrence in 'unique' list,
            # that means we found a duplicate entry!
            duplicate.append(value)
        else:
            # otherwise, that's a new value!
            unique.append(value)

    # if length of unique list is bigger than 1,
    # we have duplicates in this list!
    return True if len(unique) == 1 else False


def is_english(text):
    c = 0
    for char in text:
        if ord(char) > 127:
            c += 1
    return True if c <= 3 else False
