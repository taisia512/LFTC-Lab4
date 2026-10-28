
from pathlib import Path

from fa_reader import read_fa
from fa_to_rg import fa_to_rg


# define input files and test sequences
automata = {
    "Identifier": {
        "file": "identifier_fa.txt",
        "tests": ["average", "grade1", "labGrades", "_average", "2grade"]
    },
    "Integer": {
        "file": "integer_fa.txt",
        "tests": ["0", "10", "100", "007", "01"]
    },
    "Real": {
        "file": "real_fa.txt",
        "tests": ["0.5", "9.75", "10.0", "00.5", "12."]
    },
    "String": {
        "file": "string_fa.txt",
        "tests": ['"PASSED"', '"FAILED"', '"Final Grade"', '""', '"Unclosed']
    }
}


def main():
    input_folder = Path(__file__).parent / "input"

    for name, config in automata.items():
        print("=" * 60)
        print(f"FINITE AUTOMATON: {name.upper()}")
        print("=" * 60)

        # read the finite automaton
        file_path = input_folder / config["file"]
        fa = read_fa(file_path)

        print("States:", sorted(fa.states))
        print("Initial state:", fa.initial_state)
        print("Final states:", sorted(fa.final_states))
        print("Alphabet size:", len(fa.alphabet))

        # test accepted and rejected sequences
        print("\nSequence validation:")
        for sequence in config["tests"]:
            result = "ACCEPTED" if fa.accepts(sequence) else "REJECTED"
            print(f"  {sequence!r}: {result}")

        # transform FA into RG
        grammar = fa_to_rg(fa)

        print("\nREGULAR GRAMMAR:")
        grammar.display()
        print()


if __name__ == "__main__":
    main()
