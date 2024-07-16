list = [[100,200],[400,800],[1000,1400]]
# for a in list :
#     b = (a[0]+a[1])/2
#     print(b)
for aa in list :
    num = 0
    for bb in aa :
        num = num + bb
    print(num/len(aa))
# 문제가 복잡하면 쉬운 구조로 먼저 생각해서 뒤로 돌아가기
# 이렇게 풀면 좋은점이 리스트안의 리스트의 길이가 길어도 풀 수 있다.
