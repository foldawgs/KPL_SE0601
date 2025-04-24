from enum import Enum


class StudentStatusState(Enum):
    ACTIVE = "ACTIVE"
    NON_ACTIVE = "NON_ACTIVE"
    GRADUATED = "GRADUATED"
    CUTI = "CUTI"

class TriggerInputState(Enum):
    ACTIVE = "ACTIVE"
    NON_ACTIVE = "NON_ACTIVE"
    GRADUATED = "GRADUATED"
    CUTI = "CUTI"

transition = {
    StudentStatusState.ACTIVE: {
        TriggerInputState
}