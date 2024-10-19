import os
from collections import Counter
import socket

# Read file content
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Count words in a text
def word_count(text):
    words = text.split()
    return len(words), Counter(words)

# Handle contractions (splitting them)
def handle_contractions(text):
    contractions = {"I'm": "I am", "can't": "cannot", "don't": "do not", "isn't": "is not"}
    for contraction, full in contractions.items():
        text = text.replace(contraction, full)
    return text

# Get IP address of the machine running the container
def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# File paths
file1 = "/home/data/IF.txt"
file2 = "/home/data/AlwaysRememberUsThisWay.txt"

# Read and process both files
text1 = read_file(file1)
text2 = handle_contractions(read_file(file2))

# Word counts
count1, counter1 = word_count(text1)
count2, counter2 = word_count(text2)

# Grand total of words
grand_total = count1 + count2

# Top 3 most frequent words
top3_if = counter1.most_common(3)
top3_always = counter2.most_common(3)

# IP address
ip_address = get_ip_address()

# Write results to a file
output_file = "/home/data/output/result.txt"
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as f:
    f.write(f"IF.txt word count: {count1}\n")
    f.write(f"AlwaysRememberUsThisWay.txt word count: {count2}\n")
    f.write(f"Grand total of words: {grand_total}\n")
    f.write(f"Top 3 words in IF.txt: {top3_if}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top3_always}\n")
    f.write(f"IP address: {ip_address}\n")

# Print the result to console
with open(output_file, 'r') as f:
    print(f.read())
