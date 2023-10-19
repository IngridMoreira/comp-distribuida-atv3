from locust import HttpUser, TaskSet, task, between


class UserTasks(TaskSet):
    # @task
    # def img_1mb(self):
    #     self.client.get("/?post=5")

    # @task
    # def texto_400kb(self):
    #     self.client.get("/?post=8")

    @task
    def about_300kb(self):
        self.client.get("/?post=10")


class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 5)  # Define the wait time between tasks
