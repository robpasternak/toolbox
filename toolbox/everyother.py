def everyother(input_list = []):
    to_add = False
    output_list = []
    for element in input_list:
        if to_add:
            output_list.append(element)
        to_add = not to_add
    return output_list
