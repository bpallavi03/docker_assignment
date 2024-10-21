# Text File Word Count and Analysis with Docker

This repository contains a Python script that reads two text files, counts the total number of words, identifies the top 3 most frequent words in each file, and retrieves the IP address of the machine running the Docker container. The result is saved into a `result.txt` file.

## Features
- Count the total words in two text files.
- Identify the top 3 most frequent words in each file.
- Handle contractions (e.g., "don't" -> "do not").
- Retrieve and display the machine's IP address.
- Outputs the results to a `result.txt` file.

## Prerequisites

Make sure you have the following installed:
- Python 3.x
- Docker

## Process

1. Add your text files:
   - Place your two text files (`IF.txt` and `AlwaysRememberUsThisWay.txt`) in the `/home/data` directory or modify the paths in the script to match the location of your files.

2. Build and run the Docker container:

   To build the Docker image:
   ```bash
   docker build -t bagampi .
   ```

   To run the container:
   ```bash
   docker run -v $(pwd)/data:/home/data bagampi
   ```

3. The script will generate the `result.txt` file in the `/home/data/output` directory. The file will contain:
   - Word counts for both files.
   - The top 3 most frequent words in each file.
   - The machine's IP address.

## Script Overview

### `main.py`
The core Python script performs the following tasks:
- Reads two text files (`IF.txt` and `AlwaysRememberUsThisWay.txt`).
- Processes the text by splitting it into words, accounting for contractions.
- Counts the total words in each file.
- Finds the top 3 most frequent words in both files.
- Retrieves the IP address of the host machine.
- Outputs all the results into a `result.txt` file.

### Functions:
- `read_file(filepath)`: Reads and returns the content of the file.
- `split_words(text, handle_contractions)`: Splits the text into words, with optional contraction handling.
- `count_words(words)`: Counts the total number of words.
- `top_n_words(words, n)`: Returns the top `n` most frequent words.
- `get_ip_address()`: Gets the IP address of the host machine.

## Example Output

An example output of `result.txt` would look like:

```
Results for IF.txt:
Total words: 287
Top 3 most frequent words:
you: 14
If: 13
can: 12

Results for AlwaysRememberUsThisWay.txt:
Total words before splitting contractions: 223
Top 3 most frequent words:
I: 15
the: 12
will: 8

Grand total of words across both files: 510
IP Address of the container: X
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

