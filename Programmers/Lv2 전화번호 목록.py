def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            #print(phone_book[i] + " vs " + phone_book[j][0:len(phone_book[i])])
            if phone_book[j].startswith(phone_book[i]) or phone_book[i].startswith(phone_book[j]):
                return False
            else:
                break
    return True

print(solution(["119", "97674223", "1195524421"])) # False
print(solution(["123","456","789"])) # True
print(solution(["12","123","1235","567","88"])) # False
print(solution(["934793", "34", "44", "9347"])) # False
# 12, 15, 19 / 4

"""
"34", "44", "9347", "934793"
"""