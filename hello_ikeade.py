import prefect
from prefect import task, Flow

from datetime import timedelta
from prefect.schedules import IntervalSchedule

from prefect.storage import Docker
from prefect.run_configs import DockerRun

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello from ikeade")

#set schedule to every minute
schedule = IntervalSchedule(interval=timedelta(minutes=1))

with Flow("hello_ikeade", storage=Docker()) as flow:
    flow.run_config = DockerRun(labels=["ikea_de"])
    say_hello()

#flow.register(project_name="ikea_de")
flow.run()
