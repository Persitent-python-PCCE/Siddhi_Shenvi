import collections
import log_utils

entries = log_utils.read_logs("app.log")
levels = []
error_messages = []

for level, message in entries:
    levels.append(level)
    
    if level == "ERROR":
        error_messages.append(message)

counts = collections.Counter(levels)

output = "===== Log Summary =====\n"
output += f"INFO    : {counts.get('INFO', 0)}\n"
output += f"WARNING : {counts.get('WARNING', 0)}\n"
output += f"ERROR   : {counts.get('ERROR', 0)}\n"
output += f"DEBUG   : {counts.get('DEBUG', 0)}\n"
output += "\nErrors found:\n"

for error in error_messages:
    output += f"- {error}\n"

print(output.strip())

with open("log_summary.txt", "w") as out_file:
    out_file.write(output.strip())