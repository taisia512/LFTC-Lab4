# define a finite automaton and check if sequences are accepted
class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        # define the finite automaton
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def accepts(self, sequence):
        # start from the initial state
        current_states = {self.initial_state}

        # process each character
        for symbol in sequence:
            if symbol not in self.alphabet:
                return False

            next_states = set()

            # find the next states
            for state in current_states:
                next_states.update(
                    self.transitions.get((state, symbol), set())
                )

            if not next_states:
                return False

            current_states = next_states

        # check if a final state was reached
        return bool(current_states & self.final_states)
