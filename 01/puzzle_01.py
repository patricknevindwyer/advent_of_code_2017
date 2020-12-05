import sys


def matched_digits(seq):
    """
    Find all digits in the sequence that match the next digit in the sequence, returning
    a list of ints
    """
    matches = []
    
    # extend the sequence for wrapping
    seq = seq + seq[0]
    
    # start to end minus one
    for idx in range(len(seq) - 1):
        if seq[idx] == seq[idx + 1]:
            matches.append(int(seq[idx]))
    
    return matches


if __name__ == "__main__":
    
    with open(sys.argv[-1], "r", encoding="utf-8") as f:
        seq = f.read().strip()
        
    matches = matched_digits(seq)
    print(sum(matches))
        