grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for grade in grades_input:
        print(grade)
    return "Hi, I have to return something"


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input):
    sum_of_grade = grades_sum(grades_input)
    average = sum_of_grade / len(grades_input)
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0.0
    i = 0
    for score in scores:
        variance += (average - score) ** 2
        i += 1
    variance = variance / i
    return variance


def grades_std_deviation(variance):
    deviation = variance ** 0.5
    return deviation


print("The grades are:", grades,
      "\nThe sum is: ", grades_sum(grades),
      "\nThe average is: ", grades_average(grades),
      "\nTha variance is: ", grades_variance(grades),
      "\nThe standard deviation is: ", grades_std_deviation(grades_variance(grades)))
