'''
class NotesApp:
    def __init__(self):
        self.notes = {}
        self.menu()

    def menu(self):
        while True:
            print("\n===== Aplicativo de Notas =====")
            print("1. Criar uma nova nota")
            print("2. Visualizar uma nota")
            print("3. Listar todas as notas")
            print("4. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.create_note()
            elif choice == "2":
                self.view_note()
            elif choice == "3":
                self.list_notes()
            elif choice == "4":
                print("Saindo do aplicativo de notas.")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

    def create_note(self):
        title = input("Digite o título da nota: ")
        content = input("Digite o conteúdo da nota: ")
        self.notes[title] = content
        print(f"Nota '{title}' criada com sucesso!")

    def view_note(self):
        title = input("Digite o título da nota que deseja visualizar: ")
        if title in self.notes:
            print(f"\n===== {title} =====\n{self.notes[title]}\n")
        else:
            print(f"A nota '{title}' não foi encontrada.")

    def list_notes(self):
        print("\n===== Lista de Notas =====")
        for title in self.notes:
            print(f"- {title}")
        print("=========================")

if __name__ == "__main__":
    app = NotesApp()
'''

class TodoApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n===== Aplicativo de Lista de Tarefas =====")
        print("1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Remover tarefa")
        print("4. Listar tarefas")
        print("5. Sair")

    def add_task(self):
        task = input("Digite a nova tarefa: ")
        self.tasks.append({"task": task, "completed": False})
        print("Tarefa adicionada com sucesso!")

    def mark_task_completed(self):
        task_number = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")

    def remove_task(self):
        task_number = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
            print("Tarefa removida com sucesso!")
        else:
            print("Número de tarefa inválido.")

    def list_tasks(self):
        print("\n===== Lista de Tarefas =====")
        for i, task in enumerate(self.tasks, start=1):
            status = "Concluída" if task["completed"] else "Pendente"
            print(f"{i}. {task['task']} - Status: {status}")
        print("===========================")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.mark_task_completed()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                self.list_tasks()
            elif choice == "5":
                print("Saindo do aplicativo.")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
