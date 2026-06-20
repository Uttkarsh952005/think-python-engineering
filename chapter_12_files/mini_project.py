"""
Chapter 12: Mini Project - CLI Log Parser
Simulates reading a server log file to extract and count error types.
Demonstrates line-by-line processing, string parsing, and dictionary counters.
"""


def generate_mock_log(filename: str) -> None:
    """Creates a fake log file for testing."""
    logs = [
        "2023-10-01 10:00:00 INFO Server started\n",
        "2023-10-01 10:05:12 WARNING High memory usage\n",
        "2023-10-01 10:15:30 ERROR Connection timeout\n",
        "2023-10-01 10:16:00 INFO User login\n",
        "2023-10-01 10:20:45 ERROR Database locked\n",
        "2023-10-01 10:25:00 ERROR Connection timeout\n",
    ]
    with open(filename, "w") as f:
        f.writelines(logs)


def analyze_log_errors(filename: str) -> dict[str, int]:
    """
    Parses a log file line by line.
    Extracts the specific error message and counts occurrences.
    """
    error_counts = {}

    try:
        with open(filename, "r") as f:
            for line in f:
                if "ERROR" in line:
                    # Log format: YYYY-MM-DD HH:MM:SS LEVEL Message
                    # Split into 4 parts: date, time, level, message
                    parts = line.strip().split(maxsplit=3)
                    if len(parts) == 4:
                        error_msg = parts[3]
                        error_counts[error_msg] = error_counts.get(error_msg, 0) + 1

    except FileNotFoundError:
        print(f"Log file '{filename}' not found.")

    return error_counts


def main():
    log_file = "server.log"

    print("Generating mock log...")
    generate_mock_log(log_file)

    print("Analyzing log file for errors...\n")
    errors = analyze_log_errors(log_file)

    print("=== Error Summary ===")
    for msg, count in sorted(errors.items(), key=lambda item: item[1], reverse=True):
        print(f"[{count}x] {msg}")

    # Clean up
    import os

    if os.path.exists(log_file):
        os.remove(log_file)


if __name__ == "__main__":
    main()
