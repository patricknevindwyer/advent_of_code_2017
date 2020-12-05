import sys


def parse_spreadsheet(filename):
    """
    Load a spreadsheet as a list of lists
    """
    rows = []
    
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    for line in raw.split("\n"):
        if "\t" in line:
            cells = line.strip().split("\t")
        else:
            cells = line.strip().split(" ")
        rows.append([int(c) for c in cells])
    
    return rows
    
    
def row_checksum(row):
    """
    Take a row, compute checksum
    """
    return max(row) - min(row)


def spreadsheet_checksum(sheet):
    carry = []
    for row in sheet:
        carry.append(row_checksum(row))
    return sum(carry)


if __name__ == "__main__":
    sheet = parse_spreadsheet(sys.argv[-1])
    cs = spreadsheet_checksum(sheet)
    print("checksum: %d" % (cs,))