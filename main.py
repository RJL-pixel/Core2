

def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return [*todo_list]

    return add_todo, get_all


add, get = notebook()

add('gшпггш')
add('79897')
l = get()
print(l)




# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки.
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція.


def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        res = func(*args, **kwargs)
        print(f'{count=}')
        print('*' * 20)
        return res

    return inner



@count_decor
def expanded_form(num: int) -> str:
    st = str(num)
    print(st)
    return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0') + f' = {st}'


print(expanded_form(2525))
print(expanded_form(197860))

