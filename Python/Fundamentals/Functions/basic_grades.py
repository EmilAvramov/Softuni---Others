grade_data = float(input())


def grades(grade):
    if grade <= 2.99:
        print("Fail")
    elif 3 <= grade <= 3.49:
        print("Poor")
    elif 3.50 <= grade <= 4.49:
        print("Good")
    elif 4.50 <= grade <= 5.49:
        print("Very Good")
    else:
        print("Excellent")

        
grades(grade_data)
