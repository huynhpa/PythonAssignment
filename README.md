# DAP304x Assignment 1: Exam Grading Program

## Overview
This project is developed for the DAP304x course to create a Python program that grades exams based on input data files. The program processes student answers, validates data, calculates scores, generates statistical reports, and outputs results to a file.

## Features
- **Task 1**: Prompts the user to input a class file name (e.g., `class1` for `class1.txt`) and checks its existence using `try/except`.
- **Task 2**: Validates data lines, reporting errors for invalid lines (incorrect number of values or invalid student IDs).
- **Task 3**: Grades exams using a predefined answer key, calculates statistics (high scores, mean, highest/lowest scores, range, median), and identifies questions most skipped or answered incorrectly.
- **Task 4**: Saves student IDs and scores to an output file (e.g., `class1_grades.txt`).
- **Task 5**: Utilizes only `pandas` and `numpy` for data processing and file output.

## File Structure
- `lastname_firstname_grade_the_exams.py`: The main Python script implementing the grading logic.
- Input files (e.g., `class1.txt`, `class2.txt`): Sample data files containing student answers (not included in submission).
- Output files (e.g., `class1_grades.txt`): Generated files containing student IDs and scores.

## Requirements
- Python 3.9
- Libraries: `pandas`, `numpy`

## Installation
1. Install Python 3.9.
2. Install required libraries:
   ```bash
   pip install pandas numpy
   How to RunPlace input data files (e.g., class1.txt) in the same directory as the script.
Run the program:bash

python lastname_firstname_grade_the_exams.py

Enter the class file name (e.g., class1) when prompted.
The program will:Validate the input file and data.
Grade exams and display statistical reports.
Generate an output file (e.g., class1_grades.txt) with student IDs and scores.

Submission DetailsFolder Name: DAP304x_asm1_<YourAccount> (e.g., DAP304x_01_huynhpaFX76037@funix.edu.vn)
Files Included:lastname_firstname_grade_the_exams.py
README.md

Format: The folder is zipped into a .zip file for submission.
Note: Input and output data files are not included in the submission unless specified.

NotesThe program handles invalid data with detailed error messages.
Floating-point values (e.g., mean, median, percentages) are rounded to 3 decimal places.
The output file format contains student IDs and scores, separated by commas, without headers.

