#  Note: Still needs to be updated as current solution gets 86/100 in Judge


from project.student_report_card import StudentReportCard
import unittest


class StudentReportCardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.card = StudentReportCard('Bobi', 10)

    def test_init(self):
        student_name = 'Bobi'
        school_year = 10
        grades = {}
        self.assertEqual(student_name, self.card.student_name)
        self.assertEqual(school_year, self.card.school_year)
        self.assertDictEqual(grades, self.card.grades_by_subject)

    def test_name_setter_valid(self):
        student_name = 'Dean'
        self.card.student_name = student_name
        self.assertEqual(student_name, self.card.student_name)

    def test_name_setter_error(self):
        error_text = "Student Name cannot be an empty string!"
        student_name = ''

        with self.assertRaises(ValueError) as context:
            self.card.student_name = student_name
        self.assertEqual(error_text, str(context.exception))

        with self.assertRaises(ValueError) as context:
            StudentReportCard(student_name, 12)
        self.assertEqual(error_text, str(context.exception))

    def test_school_year_setter_valid(self):
        school_year = 9
        self.card.school_year = school_year
        self.assertEqual(school_year, self.card.school_year)

    def test_school_year_less_than_1(self):
        error_text = "School Year must be between 1 and 12!"
        school_year = 0

        with self.assertRaises(ValueError) as context:
            self.card.school_year = 0
        self.assertEqual(error_text, str(context.exception))

        with self.assertRaises(ValueError) as context:
            StudentReportCard('Test', school_year)
        self.assertEqual(error_text, str(context.exception))

    def test_school_year_more_than_12(self):
        error_text = "School Year must be between 1 and 12!"
        school_year = self.card.school_year

        with self.assertRaises(ValueError) as context:
            self.card.school_year = 130
        self.assertEqual(error_text, str(context.exception))
        self.assertEqual(school_year, self.card.school_year)

    def test_add_grade_method(self):
        self.card.grades_by_subject = {}

        retval = self.card.add_grade('Math', 6)
        self.assertIsNone(retval)

        self.card.add_grade('Math', 5)
        self.card.add_grade('English', 5.6)

        expected = {'Math': [6, 5], 'English': [5.6]}
        self.assertDictEqual(expected, self.card.grades_by_subject)

    def test_average_grades_method(self):
        self.card.grades_by_subject = {}

        expected = ''
        self.assertEqual(expected, self.card.average_grade_by_subject())

        self.card.add_grade('Math', 6)
        self.card.add_grade('Math', 4)
        self.card.add_grade('English', 5.6)
        self.card.add_grade('English', 3.6)

        expected = "Math: 5.00\nEnglish: 4.60"
        self.assertEqual(expected, self.card.average_grade_by_subject())

    def test_average_grades_all_subjects_method(self):
        self.card.grades_by_subject = {}

        self.card.add_grade('Math', 6)
        self.card.add_grade('Math', 4)
        self.card.add_grade('English', 5.6)

        expected = 'Average Grade: 5.20'
        self.assertEqual(expected, self.card.average_grade_for_all_subjects())

    def test_repr(self):
        self.card.grades_by_subject = {}
        self.card.add_grade('Math', 6)
        self.card.add_grade('Math', 4)
        self.card.add_grade('English', 5.6)

        report = f"Name: Bobi\n" \
                 f"Year: 10\n" \
                 f"----------\n" \
                 f"Math: 5.00\n" \
                 f"English: 5.60\n" \
                 f"----------\n" \
                 f"Average Grade: 5.20"
        self.assertEqual(report, repr(self.card))


if __name__ == '__main__':
    unittest.main()
