from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("test")

    def test_constructor_no_courses(self):
        self.assertEqual(self.student.name, "test")
        self.assertEqual(self.student.courses, {})

    def test_constructor_with_courses(self):
        self.student2 = Student("test2", {"course_name": ["notes"]})
        self.assertEqual(self.student2.name, "test2")
        self.assertEqual(self.student2.courses, {"course_name": ["notes"]})

    def test_add_course_no_notes(self):
        self.assertEqual(
            "Course has been added.",
            self.student.enroll("course", ["notes"], "No"),
        )
        self.assertEqual(len(self.student.courses), 1)
        self.assertEqual(self.student.courses["course"], [])

    def test_add_course_notes_Y(self):
        self.assertEqual(
            "Course and course notes have been added.",
            self.student.enroll("course", ["notes"], "Y"),
        )
        self.assertEqual(len(self.student.courses), 1)
        self.assertEqual(self.student.courses["course"], ["notes"])

    def test_add_course_notes_empty(self):
        self.assertEqual(
            "Course and course notes have been added.",
            self.student.enroll("course", ["notes"], ""),
        )
        self.assertEqual(len(self.student.courses), 1)
        self.assertEqual(self.student.courses["course"], ["notes"])

    def test_add_duplicate_course(self):
        self.student.enroll("course", ["test"])
        self.assertEqual(
            self.student.enroll("course", ["test2"]),
            "Course already added. Notes have been updated.",
        )
        self.assertEqual(len(self.student.courses["course"]), 2)
        self.assertEqual(self.student.courses["course"], ["test", "test2"])
        self.assertEqual(len(self.student.courses), 1)

    def test_add_notes_success(self):
        self.student.enroll("course", ["test"])
        self.assertEqual(
            self.student.add_notes("course", ["notesNotes"]),
            "Notes have been updated",
        )
        self.assertEqual(len(self.student.courses["course"]), 2)

    def test_add_notes_failure(self):
        with self.assertRaises(Exception) as e:
            self.student.add_notes("course", ["notes"])

        self.assertEqual(
            str(e.exception), "Cannot add notes. Course not found."
        )

    def test_remove_course_success(self):
        self.student.enroll("course", ["test"])
        self.assertEqual(
            self.student.leave_course("course"), "Course has been removed"
        )
        self.assertEqual(len(self.student.courses), 0)

    def test_remove_course_failure(self):
        with self.assertRaises(Exception) as e:
            self.student.leave_course("course")

        self.assertEqual(
            str(e.exception), "Cannot remove course. Course not found."
        )


if __name__ == "__main__":
    main()
