import re
import redaction_config

with open("report.txt") as file:
    text = file.read()

counts = {}

for term in redaction_config.SENSITIVE:
    matches = re.findall(term, text, re.IGNORECASE)
    counts[term] = len(matches)
    
    text = re.sub(term, "[REDACTED]", text, flags=re.IGNORECASE)

with open("report_redacted.txt", "w") as out_file:
    out_file.write(text)

print("Redaction complete.")
for term, count in counts.items():
    print(f"{term} -> {count} occurrences redacted")
print("Output saved to report_redacted.txt")