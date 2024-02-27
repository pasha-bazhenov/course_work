class Operation:
    def __init__(self, operation):
        self.operation = operation

    def date(self):
        """Вывод даты и типа операции."""
        date_ = f"{self.operation['date'][8:10]}.{self.operation['date'][5:7]}.{self.operation['date'][0:4]}"
        description_ = self.operation['description']
        return f"{date_} {description_}"

    def from_to(self):
        """Вывод откуда -> куда."""
        if 'from' in self.operation:
            s2 = ''.join([x for x in self.operation['from'] if not x.isdigit()])
            numbers = ''.join(c if c.isdigit() else ' ' for c in self.operation['from']).split()
            from_ = f"{s2} {numbers[0][0:4]} {numbers[0][4:6]}** **** {numbers[0][-4::]}"
            to_ = f"-> {self.operation['to'][0:4]} **{self.operation['to'][-4::]}"
            return f"{from_} {to_}"
        else:
            to_ = f"{self.operation['to'][0:4]} **{self.operation['to'][-4::]}"
            return to_

    def amount(self):
        """Вывод суммы операции и валюты."""
        return f"{self.operation['operationAmount']['amount']} {self.operation['operationAmount']['currency']['name']}"