from markov_python.cc_markov import MarkovChain

file = "pg1661.txt"

mc = MarkovChain()
mc.add_file(file)
print mc.generate_text().items