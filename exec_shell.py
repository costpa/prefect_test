import prefect
from prefect import task, Flow

#from prefect.storage import Docker
from prefect.run_configs import DockerRun


@task
def exec_shell_script():
    logger = prefect.context.get("logger")
    logger.info("I run a shell script now")
    subprocess.call(['sh', './date_to_text.sh'])

with Flow("exec_shell") as flow:
    #config run for docker and labels
    flow.run_config = DockerRun(labels=["ikea_de"])
    exec_shell_script()

#flow.register(project_name="ikea_de")
flow.run()
