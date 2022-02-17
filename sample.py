def main() -> None:
    a = 2
    b = 7
    res = calc_sum(a, b)
    print(res)


def calc_sum(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    main()
