import prefect
from prefect import task, Flow

from prefect.storage import Docker
from prefect.run_configs import DockerRun

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, It's me from the git")

with Flow("flow_from_git", storage=Docker()) as flow:
    flow.run_config = DockerRun(labels=["intern_dev"])
    say_hello()

flow.register(project_name="intern")
#flow.run()

