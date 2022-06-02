males = ['abe', 'billy', 'christian']
females = ['raven', 'willow', 'betsy']

pairs = [(male, female) for male in males for female in females]

for pair in pairs:
    print(pair)