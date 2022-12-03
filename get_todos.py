def getTodos():
    with open("docs.txt", "r") as file:
        data = file.readlines()
    return data


def writeTodos(adder):
    with open("docs.txt", "w") as file:
        file.writelines(adder)
