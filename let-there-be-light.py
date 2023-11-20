from lambeq import BobcatParser, Rewriter, AtomicType, IQPAnsatz
from pytket.circuit.display import render_circuit_jupyter, view_browser
from pytket.extensions.qiskit import tk_to_qiskit

#define atomic types
N = AtomicType.NOUN
S = AtomicType.SENTENCE

#setup ansatz
ansatz = IQPAnsatz({N: 1, S:1}, n_layers=2)

#API tools
parser = BobcatParser(verbose='suppress')
rewriter = Rewriter(['prepositional_phrase', 'determiner'])
curry_functor = Rewriter(['curry'])

#parse sentences into initial diagrams
genesis = parser.sentence2diagram('God said let there be light')
john = parser.sentence2diagram('The Word became flesh')

#create diagrams with rewrite rules, if applicable
rewritten_genesis = rewriter(genesis) #there aren't prepositional phrases...
rewritten_john = rewriter(john)

#create normalized diagrams
normalized_genesis = rewritten_genesis.normal_form()
normalized_john = rewritten_john.normal_form()

#curry diagrams and produce their normal forms
curried_genesis = curry_functor(normalized_genesis)
c_normalized_genesis = curried_genesis.normal_form()
curried_john = curry_functor(normalized_john)
c_normalized_john = curried_john.normal_form()

#draw DisCoCat diagrams. Comment out unneeded diagrams.
#genesis.draw()
#rewritten_genesis.draw()
#normalized_genesis.draw()
#curried_genesis.draw()
#c_normalized_genesis.draw()

#john.draw()
#rewritten_john.draw()
#normalized_john.draw()
#curried_john.draw()
#draw quantum circuits using diagram and ansatz (unformatted)
genesis_circuit = ansatz(c_normalized_genesis)
john_circuit = ansatz(c_normalized_john)
#genesis_circuit.draw()
#john_circuit.draw()

#format quantum circuit diagrams for readable display
genesis_tket = genesis_circuit.to_tk()
john_tket = john_circuit.to_tk()
genesis_qiskit = tk_to_qiskit(genesis_tket)
john_qiskit = tk_to_qiskit(john_tket)

#render circuit as tket or qiskit. Use comments to choose.
#view_browser(genesis_tket)
#view_browser(john_tket)
render_circuit_jupyter(genesis_tket)
render_circuit_jupyter(john_tket)
print(genesis_qiskit)
print(john_qiskit)