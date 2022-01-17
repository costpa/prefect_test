import prefect
from prefect import task, Flow
import subprocess

from prefect.storage import Docker
from prefect.run_configs import DockerRun

from datetime import timedelta, datetime
from prefect.schedules import IntervalSchedule

@task
def exec_shell_script():
    logger = prefect.context.get("logger")
    logger.info("I run a shell script now")
    subprocess.call(['sh', './date_to_text.sh'])

schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=1),
    interval=timedelta(minutes=1),
)    
    
with Flow("exec_shell", storage=Docker()) as flow:
    #config run for docker and labels
    flow.run_config = DockerRun(labels=["ikea_de"])
    exec_shell_script()

#flow.register(project_name="ikea_de")
flow.run()
