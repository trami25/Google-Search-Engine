# Simple Search Engine

## Overview

This project implements a basic search engine that mimics a simplified version of Google search. The search engine reads through a set of files and returns the names of files that contain the search query provided by the user.

The project explores and integrates various data structures and algorithms, including **lists**, **trees**, and **graphs**, to efficiently search through large amounts of data.

## Features

- **Search by Query**: The user inputs a search query, and the engine returns a list of file names where the query appears.
- **Multiple Data Structures**: Utilizes a combination of lists, trees, and graphs to optimize search performance.
- **Efficient Searching**: Implements various algorithms to traverse and search through files quickly.

## How It Works

The search engine uses the following process:

1. **File Preprocessing**: 
   - Files are read and stored using different data structures like lists (for sequential access), trees (for faster lookups), and graphs (for relationships between terms and files).
   - The files are indexed so that the search query can be matched quickly.

2. **Search Process**:
   - The user provides a search query.
   - The engine searches through the files and data structures to find which files contain the query.
   - It returns the names of the files where the query is found.

### Data Structures & Algorithms

- **Lists**: Used to store file contents for sequential access and simple operations.
- **Trees (Binary Search Trees or Tries)**: Used for faster searching of keywords in files, ensuring efficient querying.
- **Graphs**: Used to establish relationships between files and keywords. For instance, a graph can connect related terms and show which files they appear in together.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/simple-search-engine.git
