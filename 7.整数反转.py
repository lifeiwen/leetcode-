给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
思路1
code：
    def reverse(self, x: int) -> int:
        if x < 0:
            y = -1*int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y > 2147483648 or y<-2147483648:
            y = 0
        return y
