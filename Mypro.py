class Todo:

    menu = {'1':'Добавить дело', '2':'Список всех дел', '3':'Найти дело','4':'Выполнить дело', '5':'Повторить дело', '6':'Выйти'}


    def __init__(self):
       self.todo_items = []#список дел
        
    def add_todo(self, intems):
        self.todo_items.append(intems)
        print("Задача успешно добавлена")

        def list_items(self):
            pass

    def list(self):
        print("Список дел:")
        for item in self.todo_items:
            print(str(item.counter) + ' . ' + item.name + ' Выполнено ' + format(item.is_done))
        print()

    def find(self, name_find):
        return ((item.counter, item.name) for item in self.todo_items if item.name.find(name_find) != -1)
    
    def run(self):

        while True:
            # Заголовок программы
            print("Меню")
            # Вывод меню на экран

            # Перибираем словарь, и выводит ключ и значение
            for key, val in Todo.menu.items():
                print(key + '.' + val, end = '\n')
                
            # Спросить у пользователя какую команду выполнить
            command = input('Введите номер команды: ')

            # обработка выбора команды
            if command == '1':

                # Добавляем новое дело
                name_Todo = input("Какое дело? ") # запрашиваем у пользователя имя
                new_Todo = TodoItem(name_Todo) # Создаем элемент класса TodoItem

                self.add_todo(new_Todo)

            elif command == '2':
                # Показываем список
                self.list()
            elif command == '3':
                # Найдем дело
                key_word = input("Введите ключевое слово: ")# Запрашиваем у пользователя имя задачи для поиска по имени
                find = self.find(key_word) 
                
                for counter, val in find:
                    print(str(counter) + '.' + val)
            elif command == '4':
                # Выполняем дело
                number_todo = int(input("Номер задачи для выполнения: "))

                for item in self.todo_items:
                    if item.counter == number_todo: # Поиск по номеру задачи
                        item.check()
                        print("Задача выполнена!")
                        break
                else:
                    print(f'Задача {number_todo} не найдена')


            elif command == '5':
                # Повторить дело
                number_go = int(input("Номер дела для повторения: "))
                for item in self.todo_items:
                    if item.counter == number_todo: # Поиск по номеру задачи
                        item.uncheck()
                        print("Задача повторена!")

                        break
                else:
                    print(f'Задача {number_todo} не найдена')

            elif command == '6':
                # Выйти
                print("Программа завершена")
                break

class TodoItem:

    counter_do = 0

    def __init__(self,new_do):
        self.is_done = False
        self.name = new_do

        TodoItem.counter_do += 1
        self.counter = TodoItem.counter_do

    def check(self):
        self.is_done = True
        

    def uncheck(self):
        self.is_done = False
        

if __name__ == '__main__':
    todo = Todo()
    todo.run() 