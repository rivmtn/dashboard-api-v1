from app.member.model import Member
from app.report.model import Report
from app.setting.model import Setting


def init_models():
    Member()
    Setting()
    Report()
