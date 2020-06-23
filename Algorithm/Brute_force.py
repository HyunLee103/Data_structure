""" Brute Force : 모든 경우의 수를 대입해서 풀어보기, 가장 나이브한 방법 
                  모든 경우를 살피므로, 인풋이 큰 경우 매우 비효율적
                  하지만, 직관적이고 명확하다. 
                  따라서 효율적인 알고리즘을 생각하기 위한 시작은 Brute Force 이다. """

## 두 리스트 곱의 최대 
def max_product(left_cards, right_cards):
    product = []
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            product.append(left_cards[i] * right_cards[j])
    product.sort(reverse=True)
    return product[0]

def max_product(left_cards, right_cards):
    max_value = 0
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            if max_value < left_cards[i] * right_cards[j]:
                max_value = left_cards[i] * right_cards[j]
    return max_value

print(max_product([1, 6, 5], [4, 2, 3]))


## 최소 거리 좌표 찾기
from math import sqrt

def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

def closest_pair(coordinates):
    dist = 100000
    coor = []
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                if dist > distance(coordinates[i],coordinates[j]):
                    dist = distance(coordinates[i],coordinates[j])
                    coor = [coordinates[i],coordinates[j]]
    return coor

test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))


## 강남역 폭우

def trapping_rain(buildings):
    rain = []
    for i in range(1, len(buildings)-1):
        prev = max(buildings[:i])
        post = max(buildings[i:])
        hold = min(prev,post)

        if buildings[i] < hold:
            rain.append(hold - buildings[i])
    return sum(rain)

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))