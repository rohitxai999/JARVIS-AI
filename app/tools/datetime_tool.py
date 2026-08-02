from datetime import datetime


class DateTimeTool:


    def current_time(self):

        return datetime.now().strftime(
            "%H:%M:%S"
        )


    def current_date(self):

        return datetime.now().strftime(
            "%d-%m-%Y"
        )


    def current_day(self):

        return datetime.now().strftime(
            "%A"
        )