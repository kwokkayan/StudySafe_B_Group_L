from datetime import date
class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    def to_python(self, value):
        return date.fromisoformat(value)
    def to_url(self, value):
        return value

class UIDConverter:
    regex = '[0-9]{1,10}'
    def to_python(self, value):
        return value
    def to_url(self, value):
        return value