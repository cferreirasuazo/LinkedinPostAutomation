from postautomation.celery import app

class TaskSchedulerClient():
    def delete_schedule_task(self, task_id):
        app.control.revoke(task_id, terminate=True)

    def create_schedule_task(self, task_id):
        pass