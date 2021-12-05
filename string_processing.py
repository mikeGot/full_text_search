import re

# s = 'Привет, мир'
# reg = re.compile('[^а-яА-я ]')
# print(reg.sub('', s))


def preparing_to_search(query: str) -> str:
    reg = re.compile('[^а-яА-яa-zA-Z]')
    tmp = reg.sub(" ", query)

    t = "*" + tmp.replace(" ", "* *") + "*"
    return t.replace("**", "")


if __name__ == "__main__":
    print(preparing_to_search("Маша, Mike, and ,.,аня1454%:%"))