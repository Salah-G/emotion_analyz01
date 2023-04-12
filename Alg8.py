import json

# Read in the JSON files
emotions = {}
for i in range(-3, 5):
    with open(f"{i}.json", "r") as f:
        emotions[i] = json.load(f)

# Define a list of negation words
negation_words = ["not", "never", "don't"]

# Accept batch of statements as input
statements = [
"I hate Mondays",
 "I don't love ice cream",
 "I am not afraid of spiders",
 "I like to cook diner by my self",
 "I am still optimistic about the future of our country"]

# Process each statement and count the number of words in each emotion category
results = []
for statement in statements:
    # Split statement into individual words
    words = statement.lower().split()

    # Count the number of words in each emotion category
    counts = {}
    for i in range(-3, 5):
        counts[i] = 0

    negate = False
    for word in words:
        if word in negation_words:
            negate = True
        elif negate:
            for i in range(-3, 5):
                if word in emotions[i]['words']:
                    counts[i] -= 1
            negate = False
        else:
            for i in range(-3, 5):
                if word in emotions[i]['words']:
                    counts[i] += 1

    # Find the category with the highest score
    max_score = max(counts.values())
    max_category = None
    for i in range(-3, 5):
        if counts[i] == max_score:
            max_category = emotions[i]
            break

    # Store the results for this statement
    result = {
        "statement": statement,
        "scores": counts,
        "max_category": max_category['words'][0],
        "max_score": max_score
    }
    results.append(result)

# Output the results for each statement
for result in results:
    statement = result['statement']
    max_category = result['max_category']
    max_score = result['max_score']
    print(f"Statement: {statement}")
    for i in range(-3, 5):
        print(f"{emotions[i]['weight']} ==> {emotions[i]['words'][0]}: {result['scores'][i]}")
    print(f"The statement is most closely associated with the {max_category} category, with a score of {max_score}.")


    # -3 hate ====> ? word
    # -2 sad ====> 91 word
    # -1 negative ====> ? word
    # 0 neutral ====> ? word
    # 1 positive ====> ? word
    # 2 happy ====> 253 word
    # 3 love ====> 92 word
    # 4 surprise ====> 122 word