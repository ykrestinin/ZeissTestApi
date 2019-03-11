from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)

    def status(self):
        self.client.get("/status")

    @task(2)
    def registry(self):
        self.client.get("/registry")

    @task(1)
    def defined_registry(self):
        self.client.get("/registry/software")


    @task (1)
    def post_registry(self):
        self.client.post("/registry", {"serviceName":"software","verificationCode":"123"})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000