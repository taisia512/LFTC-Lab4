
from pathlib import Path

from fa_reader import read_fa


# define valid and invalid test sequences
test_cases = {
    "identifier_fa.txt": {
        "valid": [
            "a", "grade", "average", "count1",
            "labGrades", "grade_list", "x_"
        ],
        "invalid": [
            "", "_grade", "2count", "123",
            "grade-name", "a.b", "hello world"
        ]
    },
    "integer_fa.txt": {
        "valid": [
            "0", "1", "9", "10", "100", "123"
        ],
        "invalid": [
            "", "00", "007", "01", "-5",
            "12.5", "123abc", "12."
        ]
    },
    "real_fa.txt": {
        "valid": [
            "0.0", "0.5", "1.0", "9.75",
            "10.0", "100.25"
        ],
        "invalid": [
            "", "12", "12.", ".5", "00.5",
            "01.2", "9.5.2", "-1.5", "1.2abc"
        ]
    },
    "string_fa.txt": {
        "valid": [
            '""', '"PASSED"', '"FAILED"',
            '"Final Grade"', '"Grade: 10"',
            '"Hello World!"', '"123"'
        ],
        "invalid": [
            "", "PASSED", '"Unclosed',
            'Unopened"', '"PASSED"FAILED"',
            '"Hello\nWorld"'
        ]
    }
}


def main():
    input_folder = Path(__file__).parent / "input"

    total_tests = 0
    passed_tests = 0

    for filename, cases in test_cases.items():
        # read the finite automaton
        fa = read_fa(input_folder / filename)

        print("=" * 50)
        print(f"TESTING: {filename}")
        print("=" * 50)

        for sequence in cases["valid"]:
            # check valid sequences
            result = fa.accepts(sequence)
            status = "PASS" if result else "FAIL"

            print(f"{status}: {sequence!r} - expected ACCEPTED")

            total_tests += 1
            if result:
                passed_tests += 1

        for sequence in cases["invalid"]:
            # check invalid sequences
            result = fa.accepts(sequence)
            status = "PASS" if not result else "FAIL"

            print(f"{status}: {sequence!r} - expected REJECTED")

            total_tests += 1
            if not result:
                passed_tests += 1

        print()

    print("=" * 50)
    print(f"TOTAL: {passed_tests}/{total_tests} tests passed")
    print("=" * 50)


if __name__ == "__main__":
    main()
