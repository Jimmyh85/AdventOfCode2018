import solution


def test_part1():
    assert solution.part1([
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2"
    ]) == 4

    assert solution.part1([
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 3,3: 1x1"
    ]) == 4

    assert solution.part1([
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 1,3: 1x2"
    ]) == 6
