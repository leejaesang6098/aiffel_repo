import random


class FunnyDice:
    def __init__(self, n=6):  # n의 값을 입력하지 않을 시 기본값은 6
        self.n = int(n)  # 정수 처리
        self.val = random.randrange(1, self.n + 1)  # 1 <= n < (n + 1) 최종 출력값 밸류에 바로 랜덤기능을 적용

    def getval(self):
        return self.val  # getter기능을 사용해서 외부에서 이 클래스에 접근할 때 해당 메서드를 사용하게 함


def throw(): #throw 함수와 main 함수를 합침
    n = int(input())
    dice = FunnyDice(n)
    print(f"행운의 숫자는? {dice.getval()}")


if __name__ == '__main__':
    throw()
