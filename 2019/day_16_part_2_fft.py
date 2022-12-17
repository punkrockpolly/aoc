from itertools import cycle, accumulate


DAY_16_INPUT = "59702216318401831752516109671812909117759516365269440231257788008453756734827826476239905226493589006960132456488870290862893703535753691507244120156137802864317330938106688973624124594371608170692569855778498105517439068022388323566624069202753437742801981883473729701426171077277920013824894757938493999640593305172570727136129712787668811072014245905885251704882055908305407719142264325661477825898619802777868961439647723408833957843810111456367464611239017733042717293598871566304020426484700071315257217011872240492395451028872856605576492864646118292500813545747868096046577484535223887886476125746077660705155595199557168004672030769602168262"  # noqa

TEST_INPUTS = [('03036732577212944063491565474664', 100, [8, 4, 4, 6, 2, 0, 2, 6]),
               ('02935109699940807407585447034323', 100, [7, 8, 7, 2, 5, 2, 7, 0]),
               ('03081770884921959731165446850517', 100, [5, 3, 5, 5, 3, 7, 3, 1]),
               ]


def fft(puzzle_input, phases):
    offset = int(puzzle_input[:7])
    puzzle_array = [int(i) for i in puzzle_input]
    l = 10000 * len(puzzle_array) - offset
    i = cycle(reversed(puzzle_array))
    repeating_pattern = [next(i) for _ in range(l)]

    for _ in range(phases):  # loop through phases
        repeating_pattern = [n % 10 for n in accumulate(repeating_pattern)]
    return repeating_pattern[-1:-9:-1]


for (test_in, phases, test_out) in TEST_INPUTS:
    print(test_in)
    output = fft(test_in, phases)
    print("output: ", output)
    assert output == test_out

print(fft(DAY_16_INPUT, 100))