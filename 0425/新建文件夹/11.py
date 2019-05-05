# 五.哲学家吃饭问题
#
# 问题描述：    1.
# 场景是有一张圆桌， 5位哲学家围坐圆桌吃饭。 问题是每位哲学家之间的位置只有1根筷子，即圆桌上5位哲学家和5支筷子
# 2.
# 开始吃饭时，每位哲学家首先伸手去拿左手边的筷子，拿到左手边筷子的哲学家，再伸手去抢右手边的筷子。如果两支筷子都抢到，就可以吃一口饭，然后把两只筷子放下，
# 之后进行下一轮；如果没有抢到右手边的筷子，就放下左手边的筷子，此轮不吃饭。如此进行。
#
# 请用多线程和锁用代码实现此场景。
#１带入
import threading
#2
def leg():
    print(1)

def ralas():
    print(1)


if __name__ == '__main__':
    leg_thread = threading.Thread(target=leg)
    ralas_thread = threading.Thread(target=ralas)
    leg_thread.start()
    ralas_thread.start()