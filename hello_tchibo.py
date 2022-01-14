import prefect
from prefect import task, Flow

from prefect.storage import Docker
from prefect.run_configs import DockerRun

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello from ikeade")

with Flow("hello_tchibo", storage=Docker()) as flow:
    flow.run_config = DockerRun(labels=["tchibo"])
    say_hello()

#flow.register(project_name="tchibo")
flow.run()
