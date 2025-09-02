#!/usr/bin/env python
import sys
import csv

filepath = "D:/주혁/PythonProject/text/score.csv"

def load_from_csv(filepath):
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader)

        for row in csv_reader:
            student_scores[row[0]] = row[1:]
    return student_scores, header[1:]

student_scores, subjects = load_from_csv(filepath)



def subject_average(student_scores: dict, subjects: list):
    """
    이 반의 각 과목별 평균을 구해서 딕셔너리로 반환
    예) {"국어": 80.8, "수학": 35.3, "영어": 96.6, "과학": 85.3, "사회": 38.8}
    """

    sub_avg = {}
    for j in range(len(subjects)):
        sum = 0
        for i in student_scores.values():
            sum += int(i[j])

        sub_avg[subjects[j]] = float(f'{sum/len(student_scores.keys()):.1f}')

    return sub_avg

s = subject_average(student_scores, subjects)
print(f'{s}')



def student_average(student_scores: dict, subjects: list):
    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """
    stu_ave = []
    for k, l in student_scores.items():
        stu_sum = 0
        for m in l:
            stu_sum += int(m)
            ave = float(f'{stu_sum/len(subjects):.1f}')
        stu_ave.append((k, ave))
    return sorted(stu_ave, key=lambda x: x[1])
sa = student_average(student_scores, subjects)
print(sa)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <csv_file>")
        sys.exit()

    student_scores, subjects = load_from_csv(sys.argv[1])
    sub_avg = subject_average(student_scores, subjects)
    stud_avg = student_average(student_scores, subjects)

    print("과목 평균:")
    for sub, avg in sub_avg.items():
        print(f"\t{sub}: {avg:.2f}")

    print("학생 점수:")
    for avg in stud_avg:
        print(f"\t{avg[0]}: {avg[1]:.2f}")
