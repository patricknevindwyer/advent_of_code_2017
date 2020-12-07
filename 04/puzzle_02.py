import sys


def read_passphrases(filename):
    phrases = []
    
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    for line in raw.split("\n"):
        phrases.append(line.strip().split(" "))
    
    return phrases


def is_valid_phrase(phrase):
    
    found = set()
    
    for p in phrase:
        # sort the phrase
        s_p = sorted_phrase(p)
        
        if s_p in found:
            return False
        found.add(s_p)
    return True


def sorted_phrase(p):
    lets = [c for c in p]
    return "".join(sorted(lets))


if __name__ == "__main__":
    phrases = read_passphrases(sys.argv[-1])
    v_phrases = [phrase for phrase in phrases if is_valid_phrase(phrase)]
    print("%d valid" % (len(v_phrases),))