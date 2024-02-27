from functions.funcs import open_js, last_executed_operation, sort_by_date
from classes.class_operation import Operation
open_file = open_js("./functions/operations.json")
list_date = sort_by_date(open_file)
last_executed_operations = last_executed_operation(list_date)

# Список 5ти последних одобренных операций.
sort_list = last_executed_operation(list_date)
# Цикл для выводла операций в нужном формате
for i in sort_list:
    transaction = Operation(i)
    print(transaction.date())
    print(transaction.from_to())
    print(f"""{transaction.amount()}
    """)