import sys


def matched_digits(seq):
    """
    Find all digits in the sequence that match the next digit in the sequence, returning
    a list of ints
    """
    matches = []
    
    # halfway wrap of the list
    half = len(seq) / 2
    
    # start to end minus one
    for idx in range(len(seq)):
        dig_a = seq[idx]
        dig_b = seq[int((idx + half) % len(seq))]
        if dig_a == dig_b:
            matches.append(int(dig_a))
    
    return matches


if __name__ == "__main__":
    
    with open(sys.argv[-1], "r", encoding="utf-8") as f:
        seq = f.read().strip()
        
    matches = matched_digits(seq)
    print(sum(matches))
        