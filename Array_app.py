def Array_append(Array, element):
    if Array.size < Array.maxSize:
        Array.size += 1
        Array.content.append(element)
    else:
        print("Массив уже заполнен! Элемент не будет записан")
