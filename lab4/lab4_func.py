def func(x):
    """root x=1.180"""
    return x**3+2*x-4


def search(f, neg_point, pos_point, accuracy):
    mid_point = (neg_point + pos_point) / 2
    if abs(neg_point - pos_point) < accuracy:
        return mid_point
    test_value = f(mid_point)
    if test_value > 0:
        return search(f, neg_point, mid_point, accuracy)
    elif test_value < 0:
        return search(f, mid_point, pos_point, accuracy)
    return mid_point


def half_interval_method(f, a, b, e):
    """метод половинного ділення"""
    a_val = f(a)
    b_val = f(b)
    if a_val > 0 > b_val:
        return search(f, b, a, e)
    elif a_val < 0 < b_val:
        return search(f, a, b, e)
    else:
        return 'Error'
