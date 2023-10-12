# Import Statements
import questions

def main():
    """
    Creates a question list using for loops and if-else to keep tally of correct answers as
    well as prompting the user for input. The if-else checks if the answer is correct and returns
    correct or incorrect responses depending on the answer.
    """
    correct = 0
    # Create a question list.
    quests = get_questions()

    for i in range(10):
        current = quests[i]
        print(current)
        user_answer = int(input('Enter your solution (a number between 1 and 4): '))
        if current.is_correct(user_answer):
            correct += 10
            print('\nThat is the correct answer.\n')
            print()
        else:
            print(f'\nThat is incorrect. The correct answer is {current.get_solution()}\n')
    print(f'Your score is: {correct}%\n')

def get_questions():
    """
    Creates the questions and formats them.
    """
    quests = []

    # Create list.
    question1 = questions.Question('What is the informal language, used by programmers use to\n'
                                   + 'create models of programs, that has no syntax rules and\n'
                                   + 'is not meant to be compiled or executed?',
                                   'flowchart',
                                   'algorithm',
                                   'source code',
                                   'pseudocode',
                                   4)
    quests.append(question1)

    question2 = questions.Question('A(n) __________ is a diagram that graphically depicts the\n'
                                   + 'steps that take place in a program?',
                                   'flowchart',
                                   'algorithm',
                                   'source code',
                                   'pseudocode',
                                   1)
    quests.append(question2)

    question3 = questions.Question('The __________ function reads a piece of data that has been\n'
                                   + 'entered at the keyboard and returns that piece of data,\n'
                                   + 'as a string, back to the program.',
                                   'input()',
                                   'output()',
                                   'eval_input()',
                                   'str_input()',
                                   1)
    quests.append(question3)

    question4 = questions.Question('The line continuation character is a',
                                   '#',
                                   '%',
                                   '&',
                                   '\\',
                                   4)
    quests.append(question4)

    question5 = questions.Question('Which mathematical operator is used to raise 5 to the second'
                                   + 'power in Python?',
                                   '/',
                                   '**',
                                   '^',
                                   '~',
                                   2)
    quests.append(question5)

    question6 = questions.Question('In a print statement, you can set the __________ argument to\n'
                                   + 'a space or empty string to stop the output from\n'
                                   + 'advancing to a new line.',
                                   'stop',
                                   'end',
                                   'separator',
                                   'newLine',
                                   2)
    quests.append(question6)

    question7 = questions.Question('After the execution of the following statement, the variable\n'
                                   + 'sold will reference the numeric literal value\n'
                                   + 'as (n) _______ data type.\n\nsold = 256.752',
                                   'int',
                                   'float',
                                   'str',
                                   'currency',
                                   2)
    quests.append(question7)

    question8 = questions.Question('After the execution of the following statement, the variable\n'
                                   + 'price will reference the value __________.\n\n'
                                   + 'price = int(68.549)',
                                   '68',
                                   '69',
                                   '68.55',
                                   '68.6',
                                   1)
    quests.append(question8)

    question9 = questions.Question('What is the output of the following statement?\n\n'
                                   + 'print(\'I\\\'m ready to begin\')',
                                   'Im ready to begin',
                                   'I\\\'m ready to begin',
                                   'I\'m ready to begin',
                                   '\'I\\\'m ready to begin\'',
                                   3)
    quests.append(question9)

    question10 = questions.Question('What is the output of the following statement, given that\n'
                                    + 'value1 = 2.0 and value2 = 12?\n\nprint(value1 * value2)',
                                    '24',
                                    'value1 * value2',
                                    '24.0',
                                    '2.0 * 12',
                                    3)
    quests.append(question10)

    # Return the questions
    return quests

# Call the main function.
if __name__ == '__main__':
    main()
