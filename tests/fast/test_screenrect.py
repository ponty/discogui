from discogui.screenrect import ScreenRect


def test_rect():
    assert ScreenRect(1, 2, 3, 4) == ScreenRect(1, 2, 3, 4)
    assert ScreenRect(1, 2, 3, 5) != ScreenRect(1, 2, 3, 4)

    assert ScreenRect(1, 2, 3, 4).point_inside((2, 3))
    assert not ScreenRect(1, 2, 3, 4).point_inside((2, 5))

    # point on edge -> True
    assert ScreenRect(1, 2, 3, 4).point_inside((1, 2))
