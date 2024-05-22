# Log Analyzer

This Python script is designed to analyze system logs and count the number of instances where specified patterns such as "ERROR", "WARNING" and "CRITICAL" occur in the logs.

## Dependencies

The script requires the following Python libraries, which are usually included in the standard delivery:

- re (for working with regular expressions)
- collections (to use defaultdict)

## Usage

1. edit the LOGFILE variable in the script, specifying the path to your system log file.
2. If necessary, modify the PATTERNS list by adding or removing the patterns you want to look for in the logs.
3. Run the script:

python log_analyzer.py

## Functionality
