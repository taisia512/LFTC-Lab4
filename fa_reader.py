# read finite automata from text files and create FiniteAutomaton objects
from finite_automaton import FiniteAutomaton


# expand ranges and special symbols
def expand_symbols(symbol):
    if symbol == "QUOTE":
        return {'"'}

    if symbol == "ASCII_EXCEPT_QUOTE_NEWLINE":
        return {
            chr(i) for i in range(128)
            if chr(i) not in {'"', '\n'}
        }

    if len(symbol) == 3 and symbol[1] == "-":
        start = ord(symbol[0])
        end = ord(symbol[2])

        if start > end:
            raise ValueError(f"Invalid range: {symbol}")

        return {chr(i) for i in range(start, end + 1)}

    if len(symbol) != 1:
        raise ValueError(f"Invalid symbol: {symbol}")

    return {symbol}


# read a finite automaton from a file
def read_fa(filename):
    states = set()
    alphabet = set()
    initial_state = None
    final_states = set()
    transitions = {}

    reading_transitions = False

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # skip empty lines and comments
            if not line or line.startswith("#"):
                continue

            if line == "transitions:":
                reading_transitions = True
                continue

            if reading_transitions:
                # read a transition
                state, symbol, next_state = line.split()

                for char in expand_symbols(symbol):
                    key = (state, char)

                    if key not in transitions:
                        transitions[key] = set()

                    transitions[key].add(next_state)

            elif line.startswith("states:"):
                states = set(line.split(":", 1)[1].split())

            elif line.startswith("alphabet:"):
                for symbol in line.split(":", 1)[1].split():
                    alphabet.update(expand_symbols(symbol))

            elif line.startswith("initial_state:"):
                initial_state = line.split(":", 1)[1].strip()

            elif line.startswith("final_states:"):
                final_states = set(line.split(":", 1)[1].split())

    # validate the finite automaton
    if initial_state not in states:
        raise ValueError("Invalid initial state")

    if not final_states.issubset(states):
        raise ValueError("Invalid final states")

    for (state, symbol), next_states in transitions.items():
        if state not in states:
            raise ValueError(f"Invalid transition state: {state}")

        if symbol not in alphabet:
            raise ValueError(f"Symbol not in alphabet: {symbol}")

        if not next_states.issubset(states):
            raise ValueError(f"Invalid destination state: {next_states}")

    return FiniteAutomaton(
        states,
        alphabet,
        transitions,
        initial_state,
        final_states
    )
