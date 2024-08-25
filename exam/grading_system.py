# grading_system.py

GRADING_SCALE = {
    'A+': (95, 4.0),
    'A': (90, 4.0),
    'A-': (85, 3.7),
    'B+': (80, 3.3),
    'B': (75, 3.0),
    'B-': (70, 2.7),
    'C+': (67, 2.3),
    'C': (64, 2.0),
    'C-': (60, 1.7),
    'D+': (57, 1.3),
    'D-': (50, 0.7),
    'F': (0, 0.0),
}

def get_grade_and_points(score):
    for grade, (threshold, points) in GRADING_SCALE.items():
        if score >= threshold:
            return grade, points
    return 'F', 0.0  
grade, points = get_grade_and_points(87)
print(grade)  
print(points)  