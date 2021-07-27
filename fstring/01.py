# ==============================
# Literal String Interpolation
#   3.6 Versioni
# ==============================
name = "강민석"
age = 10
print("제 나이는 {} 입니다. 제 이름은 {} 입니다.")

import datetime

date = datetime.datetime.now()
print(f"date:%Y-%m-%d-%A")

print(f'{"kms":<10}')
print(f'{"kms":>10}')
print(f'{"kms":~^10}')
print(f"{3.141592:0.2f}")
