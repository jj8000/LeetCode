class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            answer.append("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) + str(i) *
                          (i % 3 != 0 and i % 5 != 0))
        return(answer)
