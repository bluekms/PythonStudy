from collections import UserDict, UserList, UserString

# 메서드를 오버라이드 하기 좋은 자료구조


class CustomDict(UserDict):
    def contains_value(self, values):
        return values in self.data.values()


d = CustomDict()
dir(d)
d["one"] = 1
d["two"] = 2
print("one" in d)

# 값의 존재 유무를 출력하는 메서드
print(d.contains_value(1))
