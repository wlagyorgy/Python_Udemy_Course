waitling_list = ["sen", "ben", "john"]

waitling_list.sort(reverse=True)
for index, item in enumerate(waitling_list):
    print(f"{index + 1}. {item.capitalize()}")
