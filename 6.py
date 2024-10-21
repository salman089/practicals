
"""p6Implement Naive-Bayes learning algo for RWP(Restaurant Waiting Problem).
Naive Bayes is a probabilistic classification algorithm based on Bayes' Theorem, assuming that the features are conditionally independent given the class. Despite the simplicity of this assumption (which is often unrealistic), Naive Bayes works surprisingly well in many real-world scenarios, especially for text classification and spam filtering.
"""


rwp_examples = {
    'x1': {'Alt': 'Y', 'Bar': 'N', 'Fri': 'N', 'Hun': 'Y', 'Pat': 'S', 'Price': '$$$', 'Rain': 'N', 'Res': 'Y', 'Type': 'F', 'Est': '0-10', 'ans': 'Y'},
    'x2': {'Alt': 'Y', 'Bar': 'N', 'Fri': 'N', 'Hun': 'Y', 'Pat': 'F', 'Price': '$', 'Rain': 'N', 'Res': 'N', 'Type': 'T', 'Est': '30-60', 'ans': 'N'},
    'x3': {'Alt': 'N', 'Bar': 'Y', 'Fri': 'N', 'Hun': 'N', 'Pat': 'S', 'Price': '$', 'Rain': 'N', 'Res': 'N', 'Type': 'B', 'Est': '0-10', 'ans': 'Y'},
    'x4': {'Alt': 'Y', 'Bar': 'N', 'Fri': 'Y', 'Hun': 'Y', 'Pat': 'F', 'Price': '$', 'Rain': 'Y', 'Res': 'N', 'Type': 'T', 'Est': '10-30', 'ans': 'Y'},
    'x5': {'Alt': 'Y', 'Bar': 'N', 'Fri': 'Y', 'Hun': 'N', 'Pat': 'F', 'Price': '$$$', 'Rain': 'N', 'Res': 'Y', 'Type': 'F', 'Est': '>60', 'ans': 'N'},
    'x6': {'Alt': 'N', 'Bar': 'Y', 'Fri': 'N', 'Hun': 'Y', 'Pat': 'S', 'Price': '$$', 'Rain': 'Y', 'Res': 'Y', 'Type': 'I', 'Est': '0-10', 'ans': 'Y'},
    'x7': {'Alt': 'N', 'Bar': 'Y', 'Fri': 'N', 'Hun': 'N', 'Pat': 'N', 'Price': '$', 'Rain': 'Y', 'Res': 'N', 'Type': 'B', 'Est': '0-10', 'ans': 'N'},
    'x8': {'Alt': 'N', 'Bar': 'N', 'Fri': 'N', 'Hun': 'Y', 'Pat': 'S', 'Price': '$$', 'Rain': 'Y', 'Res': 'Y', 'Type': 'T', 'Est': '0-10', 'ans': 'Y'},
    'x9': {'Alt': 'N', 'Bar': 'Y', 'Fri': 'Y', 'Hun': 'N', 'Pat': 'F', 'Price': '$', 'Rain': 'Y', 'Res': 'N', 'Type': 'B', 'Est': '>60', 'ans': 'N'},
    'x10': {'Alt': 'Y', 'Bar': 'Y', 'Fri': 'Y', 'Hun': 'Y', 'Pat': 'F', 'Price': '$$$', 'Rain': 'N', 'Res': 'Y', 'Type': 'I', 'Est': '10-30', 'ans': 'N'},
    'x11': {'Alt': 'N', 'Bar': 'N', 'Fri': 'N', 'Hun': 'N', 'Pat': 'N', 'Price': '$', 'Rain': 'N', 'Res': 'N', 'Type': 'T', 'Est': '0-10', 'ans': 'N'},
    'x12': {'Alt': 'Y', 'Bar': 'Y', 'Fri': 'Y', 'Hun': 'Y', 'Pat': 'F', 'Price': '$', 'Rain': 'N', 'Res': 'N', 'Type': 'B', 'Est': '0-10', 'ans': 'Y'}
}

total_exp = len(rwp_examples)

def count(attr, val):
    return sum(1 for v in rwp_examples.values() if v[attr] == val)

def prob(attr_val, ans):
    return count(attr_val[0], attr_val[1]) / total_exp * count('ans', ans) / total_exp

def main():
    for ans in ['Y', 'N']:
        print(f"Probabilities for waiting '{ans}':")
        for attr in ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est']:
            for val in set(v[attr] for v in rwp_examples.values()):
                print(f"P({ans} | {attr}={val}): {prob((attr, val), ans):.2%}")
        print()

main()
