lexicon = {
    "north": "direction",
    "south": "direction",
    "east": "direction",
    "west": "direction",
    "go": "verb",
    "kill": "verb",
    "eat": "verb",
    "the": "stop",
    "of": "stop",
    "in": "stop",
    "bear": "noun",
    "princeness": "noun",
    "3": "number",
    "91234": "number",
    "1234": "number",
    "ASDFADFASDF": "error",
    "IAS": "error",
}


def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)
        results.append((word_type, word))
    return results
