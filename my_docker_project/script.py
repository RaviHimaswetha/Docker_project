import os
import re
import socket
from collections import Counter

# Function to count words in a text file
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []  # Return an empty list if the file is not found
    text = re.sub(r"’", "'", text)
    contractions = {
        "i'm": "i am", "can't": "cannot", "don't": "do not", "won't": "will not", 
        "you're": "you are", "it's": "it is", "let's": "let us", "i've": "i have",
        "isn't": "is not", "aren't": "are not", "couldn't": "could not"
    }
    for contraction, full in contractions.items():
        text = text.replace(contraction, full)
    words = re.findall(r'\b\w+\b', text)
    return words

# Function to get the top N frequent words
def get_top_n_frequent_words(words, n=3):
    word_counts = Counter(words)
    return word_counts.most_common(n)

# Function to get the container's IP address
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# File paths
data_dir = "/home/data"
file1_path = os.path.join(data_dir, "IF.txt")
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay.txt")
output_file_path = os.path.join(data_dir, "output", "result.txt")

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Process the files
words_file1 = count_words(file1_path)
words_file2 = count_words(file2_path)

# Count the total number of words in each file
word_count_file1 = len(words_file1)
word_count_file2 = len(words_file2)

# Calculate the grand total of words across both files
grand_total_words = word_count_file1 + word_count_file2

# Identify the top 3 most frequent words in IF.txt
top_3_words_file1 = get_top_n_frequent_words(words_file1)

# Identify the top 3 frequent words in AlwaysRememberUsThisWay.txt
top_3_words_file2 = get_top_n_frequent_words(words_file2)

# Determine the container's IP address
ip_address = get_ip_address()

# Write the results to the output file and print to console
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Word count in IF.txt: {word_count_file1}\n")
    output_file.write(f"Word count in AlwaysRememberUsThisWay.txt: {word_count_file2}\n")
    output_file.write(f"Grand total word count: {grand_total_words}\n")
    output_file.write(f"Top 3 words in IF.txt: {top_3_words_file1}\n")
    output_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_3_words_file2}\n")
    output_file.write(f"Container IP address: {ip_address}\n")

# Print the contents of result.txt to the console
with open(output_file_path, 'r') as output_file:
    print(output_file.read())
