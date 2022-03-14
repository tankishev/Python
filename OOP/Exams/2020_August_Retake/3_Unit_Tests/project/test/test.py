#  Note: Still needs to be updated as current solution gets 86/100 in Judge


from project.student_report_card import StudentReportCard
import unittest


class StudentReportCardTests(unittest.TestCase):

    def test_init(self):
        s = StudentReportCard('Bobi', 10)
        self.assertEqual(s.student_name, 'Bobi')
        self.assertEqual(s.school_year, 10)
        self.assertTrue(hasattr(s, 'grades_by_subject'))
        self.assertTrue(hasattr(s, 'student_name'))
        self.assertTrue(hasattr(s, 'school_year'))
        self.assertTrue(hasattr(s, 'add_grade'))
        self.assertTrue(hasattr(s, 'average_grade_by_subject'))
        self.assertTrue(hasattr(s, 'average_grade_for_all_subjects'))
        self.assertTrue(hasattr(s, f'_StudentReportCard__student_name'))
        self.assertTrue(hasattr(s, f'_StudentReportCard__school_year'))
        self.assertTrue(isinstance(s.grades_by_subject, dict))
        self.assertDictEqual(s.grades_by_subject, {})

    def test_prop_setters(self):
        s = StudentReportCard('Bobi', 10)
        self.assertEqual(getattr(s, f'_StudentReportCard__student_name', None), 'Bobi')
        self.assertEqual(getattr(s, f'_StudentReportCard__school_year', None), 10)
        self.assertEqual(s.student_name, 'Bobi')
        self.assertEqual(s.school_year, 10)
        s.student_name = 'Ivo'
        s.school_year = 7
        self.assertEqual(getattr(s, f'_StudentReportCard__student_name', None), 'Ivo')
        self.assertEqual(getattr(s, f'_StudentReportCard__school_year', None), 7)

    def test_student_name_raises_error_if_blank(self):
        error_text = "Student Name cannot be an empty string!"
        s = StudentReportCard('Bobi', 10)
        with self.assertRaises(ValueError) as context:
            s.student_name = ''
        self.assertTrue(error_text in str(context.exception))

        with self.assertRaises(ValueError) as context:
            s2 = StudentReportCard('', 8)
        self.assertTrue(error_text in str(context.exception))

    def test_school_year_raises_error_if_not_between_1_and_12(self):
        error_text = "School Year must be between 1 and 12!"
        s = StudentReportCard('Bobi', 10)
        with self.assertRaises(ValueError) as context:
            s.school_year = 0
        self.assertTrue(error_text in str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.school_year = 13
        self.assertTrue(error_text in str(context.exception))

        with self.assertRaises(ValueError) as context:
            s2 = StudentReportCard("Ivo", 22)
        self.assertTrue(error_text in str(context.exception))

    def test_add_grade(self):
        s = StudentReportCard('Bobi', 10)
        s.add_grade('Math', 6)
        self.assertDictEqual(s.grades_by_subject, {'Math': [6]})
        s.add_grade('Math', 5)
        self.assertDictEqual(s.grades_by_subject, {'Math': [6, 5]})
        s.add_grade('English', 5.6)
        self.assertDictEqual(s.grades_by_subject, {'Math': [6, 5], 'English': [5.6]})

    def test_average_grades(self):
        s = StudentReportCard('Bobi', 10)
        self.assertEqual(s.average_grade_by_subject(), "")
        s.add_grade('Math', 6)
        s.add_grade('Math', 4)
        self.assertEqual(s.average_grade_by_subject(), "Math: 5.00")
        s.add_grade('English', 5.6)
        self.assertEqual(s.average_grade_by_subject(), "Math: 5.00\nEnglish: 5.60")
        self.assertEqual(s.average_grade_for_all_subjects(), 'Average Grade: 5.20')

    def test_repr(self):
        student_name = 'Bobi'
        school_year = 9
        s = StudentReportCard(student_name, school_year)
        s.add_grade('Math', 6)
        s.add_grade('Math', 4)
        s.add_grade('English', 5.6)
        report = f"Name: {s.student_name}\n" \
                 f"Year: {s.school_year}\n" \
                 f"----------\n" \
                 f"{s.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{s.average_grade_for_all_subjects()}"
        self.assertEqual(repr(s), report)


if __name__ == '__main__':
    unittest.main()
