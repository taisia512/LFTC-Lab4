
class RegularGrammar:
    def __init__(self, nonterminals, terminals, productions, start_symbol):
        # define the regular grammar
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def display(self):
        # display grammar components
        print("Nonterminals:", sorted(self.nonterminals))
        print("Terminals:", [repr(symbol) for symbol in sorted(self.terminals)])
        print("Start symbol:", self.start_symbol)

        print("Productions:")
        for nonterminal in sorted(self.productions):
            rules = []

            # format each production
            for production in sorted(self.productions[nonterminal]):
                if production == "ε":
                    rules.append("ε")
                else:
                    symbol = production[0]
                    next_state = production[1:]
                    rules.append(f"{repr(symbol)} {next_state}")

            # display productions separated by |
            if rules:
                print(f"  {nonterminal} -> {' | '.join(rules)}")


# transform a finite automaton into a regular grammar
def fa_to_rg(fa):
    nonterminals = set(fa.states)
    terminals = set(fa.alphabet)
    start_symbol = fa.initial_state

    productions = {state: set() for state in fa.states}

    # convert transitions into productions
    for (state, symbol), next_states in fa.transitions.items():
        for next_state in next_states:
            productions[state].add(symbol + next_state)

    # add epsilon productions for final states
    for state in fa.final_states:
        productions[state].add("ε")

    return RegularGrammar(
        nonterminals,
        terminals,
        productions,
        start_symbol
    )
