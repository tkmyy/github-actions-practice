import argparse


def main(num_1: int, num_2: int) -> None:
    res = calc_sum(num_1, num_2)
    print(res)


def calc_sum(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_1", type=int)
    parser.add_argument("--num_2", type=int)
    args = parser.parse_args()
    num_1 = args.num_1
    num_2 = args.num_2
    main(num_1=num_1, num_2=num_2)
