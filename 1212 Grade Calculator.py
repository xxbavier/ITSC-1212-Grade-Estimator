NUM_COURSEWORK_ASSIGNMENTS = 0 # Represents the total number of coursework assignments.
COURSEWORK_POINTS = 0 # Represents the total number of points earned from coursework assignments.

def add_coursework_grades() -> None:
    '''
    Input:
        This function does not take any input parameters.
    Process:
        Prompts the user for how many quizzes they have completed.
        For each quiz, it prompts the user for their grade on the quiz.
        Adds the grade to the global variable COURSEWORK_POINTS.
        Increments the global variable NUM_COURSEWORK_ASSIGNMENTS by 1 for each quiz
    Output:
        Returns None.
    '''
    global NUM_COURSEWORK_ASSIGNMENTS
    global COURSEWORK_POINTS

    print("----------- Remainder of Coursework Grades -----------")
    num_quizzes = int(input("Enter the number for the most recent module: "))

    for i in range(num_quizzes+1):
        quiz = float(input("Enter your grade for \"Module " + str(i) + ": Quiz\" (0-100): "))/100 # Scale the grade to be out of 1 instead of 100.
        prep = float(input("Enter your grade for \"Module " + str(i) + ": Prep\" (0-1): "))
        checkout = float(input("Enter your grade for \"Module " + str(i) + ": Checkout\" (0-1): "))

        lecture = float(input(f"Enter your attendance grade for \"Module {i} Lecture Attendance\" (0-1): "))
        lab1 = float(input(f"Enter your attendance grade for \"Module {i} Lab 1 Attendance\" (0-1): "))
        lab2 = float(input(f"Enter your attendance grade for \"Module {i} Lab 2 Attendance\" (0-1): "))
        
        COURSEWORK_POINTS += quiz + prep + checkout + lab1 + lab2 + lecture
        NUM_COURSEWORK_ASSIGNMENTS += 6

        print()

    print("------------------------------------")

def add_problem_set_grades() -> float:
    '''
    Input:
        This function does not take any input parameters.
    Process:
        Prompts the user for how many problem sets they have completed.
        For each problem set, it prompts the user for their grade on the problem set.
        Adds the grade to the global variable COURSEWORK_POINTS.
        Increments the global variable NUM_COURSEWORK_ASSIGNMENTS by 1 for each problem
    Output:
        Returns None.
    '''
    global NUM_COURSEWORK_ASSIGNMENTS
    global COURSEWORK_POINTS

    print("-------- Problem Set Grades --------")
    num_problem_sets = int(input("Enter the number for the most recent problem set: "))

    for i in range(num_problem_sets+1): # Loop through the number of problem sets, start from 0 since the first Problem Set is Problem Set 0.
        grade = float(input("Enter your grade for \"Problem Set " + str(i) + "\" (0-1): "))
        
        COURSEWORK_POINTS += grade
        NUM_COURSEWORK_ASSIGNMENTS += 1
        
        print()

    print("------------------------------------")


def get_checkpoint_grade() -> float:
    '''
    Input:
        This function does not take any input parameters.
    Process:
        Prompts the user for how many problem sets they have completed.
        For every checkpoint, prompt the user for their grade.
        Typecast the grade to a float.
        Calculate the average of the checkpoint grades.
    Output:
        Returns the average of the checkpoint grades.
    '''

    print("--------- Checkpoint Grade ---------")
    num_checkpoints = int(input("Enter the number of checkpoints you have completed: "))
    
    total_grade = 0

    for i in range(num_checkpoints):
        grade = float(input("Enter your grade for Checkpoint " + str(i) + " (0-100): "))
        total_grade += grade
        print()

    print("------------------------------------")
    return total_grade/num_checkpoints # Return the average of the checkpoint grades.

def main() -> None:
    '''
    Input:
        This function does not take any input parameters.
    Process:
        Calculates the checkpoint average.
        Calculates the coursework average.
        Calculates the total grade estimate.
    Output:
        Prints the total grade estimate.
    '''
    global NUM_COURSEWORK_ASSIGNMENTS
    global COURSEWORK_POINTS

    print("------- 1212 Grade Estimator -------")
    print("Made by Xavier Engelbrecht")
    print()
    print("Disclaimer: This is not an official tool and may not be accurate. Furthermore, this tool does not take into account any of the following:")
    print(" - Engagement")
    print(" - Late submissions")
    print(" - Excused absences")
    print(" - Improvement over time")
    print()
    print()

    input("Press Enter to continue...") # Wait for user input before continuing.

    print()
    print("------------------------------------")
    print()


    # Store the checkpoint grade, and then populate the NUM_COURSEWORK_ASSIGNMENTS and COURSEWORK_POINTS variables.
    checkpoint_grade = get_checkpoint_grade()
    add_problem_set_grades()
    add_coursework_grades()

    coursework_average = (COURSEWORK_POINTS/NUM_COURSEWORK_ASSIGNMENTS) * 100

    # Display the total grade estimate.
    print("------- Total Grade Estimate -------")
    print(f"Checkpoint Grade (60%): {round(checkpoint_grade,2)}%")
    print(f"Coursework Average (40%): {round(coursework_average,2)}%")
    print(f"Estimated Total Grade: {round((checkpoint_grade * 0.6) + (coursework_average * 0.4),2)}%")
    print("------------------------------------")

main()