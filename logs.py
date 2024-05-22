import os
import re
import collections


PATTERNS = ["ERROR", "WARNING", "CRITICAL"]

def analyze_logs():
    LOGDIR = input("Enter the path to the catalog with log files: ")
  
    pattern_counts = collections.defaultdict(int)

    for filename in os.listdir(LOGDIR):
        if filename.endswith(".log"):
            with open(os.path.join(LOGDIR, filename), "r") as file:
                log_data = file.read()
            
            for pattern in PATTERNS:
                pattern_counts[pattern] += len(re.findall(pattern, log_data))
              
    for pattern, count in pattern_counts.items():
        print(f"{pattern}: {count} occurrences")


analyze_logs()
