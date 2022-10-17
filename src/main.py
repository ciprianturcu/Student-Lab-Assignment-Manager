from domain.assignments import AssignmentValidator
from domain.grade import GradeValidator
from domain.student import StudentValidator
from repository.repository import Repository
from services.assignments_service import AssignmentService
from services.grade_service import GradeService
from services.student_service import StudentService
from services.undo_service import UndoRedoService
from ui.ui import Ui

if __name__ == "__main__":
    student_validator = StudentValidator()
    student_repository = Repository()

    assignment_validator = AssignmentValidator()
    assignment_repository = Repository()

    grade_validator = GradeValidator()
    grade_repository = Repository()

    undo_redo_service = UndoRedoService()

    grade_service = GradeService(undo_redo_service, grade_repository, grade_validator, student_repository,
                                 assignment_repository)
    assignment_services = AssignmentService(undo_redo_service, assignment_repository, assignment_validator,
                                            grade_service,grade_repository)
    student_services = StudentService(undo_redo_service, student_repository, student_validator, grade_service,
                                      grade_repository)

    console = Ui(undo_redo_service, student_services, assignment_services, grade_service)
    console.start()
