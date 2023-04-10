# def get_status(is_busy):
#     return {"status": "busy" if is_busy else "available"}
#
#
# print(get_status(True))

# def remove_consecutive_duplicates(s : str) -> str:
#     set1 = set(s.split(" "))
#     lst = list(set1)
#     return str(lst)
#
#
# s = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
# print(remove_consecutive_duplicates(s))

def capitalize(s, ind):
    lst_str = list(s)
    lst_result = []
    for i in range(len(s)):
        if i in ind:
            lst_result = lst_result.append(lst_str[ind[j]].upper())
        for j in ind:
            if ind[j] >= len(s):
                return f"There is no index {ind[j]}"

    return " ".join(lst_result)


print(capitalize("collaboration", [2, 3, 10]))