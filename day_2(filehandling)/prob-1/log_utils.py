def parse_line(line):
    part = line.strip().split(maxsplit=3)
    level = part[2]
    message = part[3]
    return level, message

def read_logs(path):
    entries = []
    with open(path) as file:
        for line in file:
            parsed_entry = parse_line(line)
            entries.append(parsed_entry)
    return entries