# a, b = map(int, input().split())
# print(a+b)

# 함수형
# def plus(num_list):
#     return sum(num_list)

# if __name__ == '__main__':
#     num_list = map(int, input().split())
#     print(sum(num_list))
#     a = plus(num_list)
    
    
# 클래스
class Plus:
    def __init__(self, num_list):
        self.num_list = num_list
    
    def plus(self):
        return sum(self.number_list)
    
a = Plus(map(int, input().split()))
print(a.plus)

