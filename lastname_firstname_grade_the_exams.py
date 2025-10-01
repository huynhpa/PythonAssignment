import pandas as pd
import numpy as np

# Đáp án đúng của bài thi
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

def validate_filename():
    """Task 1: Nhập và kiểm tra tệp đầu vào"""
    while True:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        try:
            with open(f"{filename}.txt", "r") as file:
                print(f"Successfully opened {filename}.txt")
                return filename, file.read().splitlines()
        except FileNotFoundError:
            print("File cannot be found.")

def validate_data(data):
    """Task 2: Phân tích và kiểm tra dữ liệu hợp lệ"""
    valid_lines = []
    invalid_lines = []
    
    print("**** ANALYZING ****")
    for line in data:
        # Tách dòng thành danh sách các giá trị
        values = line.strip().split(",")
        
        # Kiểm tra số lượng giá trị (phải đúng 26 giá trị)
        if len(values) != 26:
            print(f"Invalid line of data: does not contain exactly 26 values:\n{line}")
            invalid_lines.append(line)
            continue
        
        # Kiểm tra định dạng N# (N + 8 số)
        student_id = values[0]
        if not (student_id.startswith("N") and len(student_id) == 9 and student_id[1:].isdigit()):
            form = "does not contain exactly 26 values" if len(values) != 26 else "N# is invalid"
            print(f"Invalid line of data: {form}:\n{line}")
            invalid_lines.append(line)
            continue
        
        valid_lines.append(line)
    
    if not invalid_lines:
        print("No errors found!")
    
    return valid_lines, invalid_lines

def grade_exams(valid_lines, filename):
    """Task 3 & 4: Chấm điểm và tạo file kết quả"""
    answer_key_list = answer_key.split(",")
    scores = []
    skip_counts = [0] * 25  # Đếm số lần bỏ qua mỗi câu hỏi
    wrong_counts = [0] * 25  # Đếm số lần trả lời sai mỗi câu hỏi
    
    # Tạo DataFrame để lưu kết quả
    results = []
    
    for line in valid_lines:
        values = line.strip().split(",")
        student_id = values[0]
        answers = values[1:]
        score = 0
        
        # Chấm điểm
        for i, (student_answer, correct_answer) in enumerate(zip(answers, answer_key_list)):
            if student_answer == "":
                skip_counts[i] += 1
                score += 0
            elif student_answer == correct_answer:
                score += 4
            else:
                wrong_counts[i] += 1
                score -= 1
        
        scores.append(score)
        results.append([student_id, score])
    
    # Tính toán thống kê
    scores = np.array(scores)
    high_scores = np.sum(scores > 80)
    mean_score = np.mean(scores)
    highest_score = np.max(scores)
    lowest_score = np.min(scores)
    range_scores = highest_score - lowest_score
    
    # Tính giá trị trung vị
    sorted_scores = np.sort(scores)
    if len(sorted_scores) % 2 == 0:
        median_score = (sorted_scores[len(sorted_scores)//2 - 1] + sorted_scores[len(sorted_scores)//2]) / 2
    else:
        median_score = sorted_scores[len(sorted_scores)//2]
    
    # Tìm câu hỏi bị bỏ qua nhiều nhất
    max_skips = max(skip_counts)
    skip_questions = [
        f"{i+1} - {skip_counts[i]} - {skip_counts[i]/len(valid_lines):.3f}"
        for i in range(25) if skip_counts[i] == max_skips
    ]
    
    # Tìm câu hỏi bị trả lời sai nhiều nhất
    max_wrongs = max(wrong_counts)
    wrong_questions = [
        f"{i+1} - {wrong_counts[i]} - {wrong_counts[i]/len(valid_lines):.3f}"
        for i in range(25) if wrong_counts[i] == max_wrongs
    ]
    
    # In báo cáo
    print("**** REPORT ****")
    print(f"Total valid lines of data: {len(valid_lines)}")
    print(f"Total invalid lines of data: {len(data) - len(valid_lines)}")
    print(f"Total student of high scores: {high_scores}")
    print(f"Mean (average) score: {mean_score:.3f}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Range of scores: {range_scores}")
    print(f"Median score: {median_score:.3f}")
    print(f"Question that most people skip: {', '.join(skip_questions)}")
    print(f"Question that most people answer incorrectly: {', '.join(wrong_questions)}")
    
    # Task 4: Lưu kết quả vào file
    results_df = pd.DataFrame(results, columns=["Student ID", "Score"])
    results_df.to_csv(f"{filename}_grades.txt", index=False, header=False)

def main():
    # Task 1: Nhập và mở tệp
    filename, data = validate_filename()
    
    # Task 2: Kiểm tra dữ liệu
    valid_lines, invalid_lines = validate_data(data)
    
    # Task 3 & 4: Chấm điểm và lưu kết quả
    if valid_lines:
        grade_exams(valid_lines, filename)

if __name__ == "__main__":
    main()