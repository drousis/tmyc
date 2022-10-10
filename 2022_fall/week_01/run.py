import operator

op_map = {
    1: operator.add,
    2: operator.mul
}


def run_int_code(int_string, noun=0, verb=0):

    ints = list(map(int, int_string.split(",")))

    ints[1] = noun
    ints[2] = verb

    for i in range(0, len(ints), 4):

        if ints[i] == 99:
            return ints

        ints[ints[i + 3]] = op_map[ints[i]](ints[ints[i + 1]], ints[ints[i + 2]])


if __name__ == "__main__":
    import itertools

    int_string_1 = (
        "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,"
        "10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,"
        "9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0"
    )

    # part 1
    print(run_int_code(int_string_1, noun=12, verb=2)[0])

    # part 2
    for noun, verb in itertools.product(range(100), range(100)):

        if run_int_code(int_string_1, noun, verb)[0] == 19690720:
            print(100 * noun + verb)
            break
