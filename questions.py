"""
ch10_ex2.py
"""
class Question:
    """
    Holds the data structure for the Question class.
    """
    def __init__(self, question, answer1, answer2, answer3, answer4, solution):
        """
        Contructor for question.
        """
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__solution = solution

    def set_questions(self, question):
        """
        Mutator for question.
        """
        self.__question = question

    def set_answer1(self, answer1):
        """
        Mutator for answer1.
        """
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        """
        Mutator for answer2.
        """
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        """
        Mutator for answer3.
        """
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        """
        Mutator for answer4.
        """
        self.__answer4 = answer4

    def set_solution(self, solution):
        """
        Mutator for solution.
        """
        self.__solution = solution

    def get_question(self):
        """
        Accessor for question.
        """
        return self.__question
    def get_answer1(self):
        """
        Accessor for answer1.
        """
        return self.__answer1
    def get_answer2(self):
        """
        Accessor for answer2.
        """
        return self.__answer2
    def get_answer3(self):
        """
        Accessor for answer3.
        """
        return self.__answer3
    def get_answer4(self):
        """
        Accessor for answer4.
        """
        return self.__answer4
    def get_solution(self):
        """
        Accessor for solution.
        """
        return self.__solution
    def __str__(self):
        """
        Returns the item.
        """
        result = '\n' + self.get_question() + '\n\n' + \
                 '1. ' + self.get_answer1() + '\n' + \
                 '2. ' + self.get_answer2() + '\n' + \
                 '3. ' + self.get_answer3() + '\n' + \
                 '4. ' + self.get_answer4() + '\n'
        return result
    def is_correct(self, answer):
        """
        Returns true correct answer or false.
        """
        return answer == self.get_solution()
    