# 함수 구현부
def add_data(data):
    lst.append = None
    lstLen = len(lst)
    lst[lstLen - 1] = data


def insert_data(idx, data):
    if idx < 0 or idx > len(lst):
        return
    else:
        lst.append = None
        lstLen = len(lst)
        for i in range(lstLen - 1, idx, -1):
            lst[i] = lst[i - 1]
            lst[i - 1] = None
        lst[idx] = data


def delete_data(idx):
    lstLen = len(lst)
    if idx >= lstLen or idx < 0:
        return
    else:
        lst[idx] = None
        for i in range(idx, lstLen - 1):
            lst[i] = lst[i + 1]
            lst[i + 1] = None
        del(lst[lstLen - 1])

# 전역 변수 선언부
lst = []

# 메인 구현부
