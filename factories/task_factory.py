from models import Task

class TaskFactory:
    @staticmethod
    def create_task(title: str, description: str = None, completed: bool = False, icon: str = "📌"):
        """Método estático para crear tareas de manera modular."""
        return Task(title=title, description=description, completed=completed, icon=icon)
