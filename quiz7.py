num1 = []
num2 = []
num3 = []
for i in range(0,101):
    if i%2 == 0 :
        num1.append(i)
    if i%3 == 0 :
        num2.append(i)
    if i%5 == 0 :
        num3.append(i)
print(num1)
print(num2)
print(num3)

# 2의 배수로 골라네는 법 (if)
# if a % 2 == 0 :
# # 리스트 함수에 저장하는 법 (append)
# numbers = []
# numbers.append(1)
# 1부터 100까지 반복적으로 수행하는 법(for,while)