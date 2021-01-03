def cheak(x1, x2, x3):
    if x1 > 0 and x2 % 3 != 0 and x1 <= x2 and x1 <= x3:
        return True
    else:
        return False


def need(x1, x2):
    return max(x1, x2)-min(x1, x2)


def subwey():
    sum_of_road, dif, minimal_dif = 0, 0, 0
    for i in range(5):
        x1, x2, x3 = map(int, input().split())
        sum_of_road += max(x1, x2, x3)
        q, w, e = need(x1, x2), need(x2, x3), need(x1, x3)
        if cheak(q, w, e):
            minimal_dif = q
        elif cheak(w, q, e):
            minimal_dif = w
        elif cheak(e, q, w):
            minimal_dif = e

        if minimal_dif != 0:
            dif = minimal_dif

        if minimal_dif < dif:
            dif = minimal_dif

    if sum_of_road % 3 == 0 and dif == 0:
        print('Save me!')
    elif sum_of_road % 3 == 0 and dif != 0:
        print(sum_of_road - dif)
    else:
        print(sum_of_road)


def main():
    subwey()