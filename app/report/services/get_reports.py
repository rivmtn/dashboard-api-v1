from sqlalchemy.orm import Session

from app.report.model import Report
from app.report.schema import ReportRowDto, ReportSumDto
from app.setting.model import Setting
from app.util.response import response, Message
from app.util.token_checker import token_checker


@token_checker
def get_reports(**kwargs):
    db: Session = kwargs.get("db")
    sdate = kwargs.get("sdate")
    edate = kwargs.get("edate")

    origin_data = db.query(Report).filter(Report.day >= sdate, Report.day <= edate).all()

    settings = db.query(Setting).order_by(Setting.start_date).all()

    custom_data = []
    sum_imp = 0
    sum_click = 0
    sum_sale = 0
    sum_order_cnt = 0
    sum_cancel_cnt = 0
    sum_revenue = 0
    for i in origin_data:
        day = i.day
        imp = i.imp
        click = i.click
        sale = i.sale
        order_cnt = i.order_cnt
        cancel_cnt = i.cancel_cnt
        revenue = i.revenue

        ratio = next(
            (setting.ratio for setting in settings if setting.start_date <= int(day) <= setting.end_date),
            100,
        )

        custom_click = round(int(click) * ratio / 100)
        custom_sale = round(int(sale) * ratio / 100)
        custom_revenue = round(int(revenue) * ratio / 100)

        sum_imp += int(imp)
        sum_click += int(custom_click)
        sum_sale += int(custom_sale)
        sum_order_cnt += int(order_cnt)
        sum_cancel_cnt += int(cancel_cnt)
        sum_revenue += int(custom_revenue)

        custom_data.append(
            ReportRowDto(
                day=str(day),
                imp=str(imp),
                click=str(custom_click),
                sale=str(custom_sale),
                order_cnt=str(order_cnt),
                cancel_cnt=str(cancel_cnt),
                revenue=str(custom_revenue),
            )
        )

    sorted_data = sorted(
        custom_data,
        key=lambda x: int(x.day),
        reverse=True,
    )

    summary: ReportSumDto = ReportSumDto(
        imp=sum_imp,
        click=sum_click,
        sale=sum_sale,
        order_cnt=sum_order_cnt,
        cancel_cnt=sum_cancel_cnt,
        revenue=sum_revenue,
    )

    return response(
        message=Message.SUCCESS.value,
        data=sorted_data,
        summary=summary,
    )
