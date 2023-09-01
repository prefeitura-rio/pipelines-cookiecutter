# -*- coding: utf-8 -*-
from prefect import Flow, Parameter
from prefect.run_configs import KubernetesRun
from prefect.storage import GCS

from pipelines.constants import constants
from pipelines.exemplo.nome_do_objetivo.tasks import greet

with Flow(
    name="{{ cookiecutter.project_name }}: Nome do objetivo - Descrição detalhada do objetivo",
) as exemplo__nome_do_objetivo__greet_flow:
    # Parameters
    name = Parameter("name", default="{{ cookiecutter.project_slug }}")

    # Tasks
    greet_task = greet(name)

# Storage and run configs
exemplo__nome_do_objetivo__greet_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
exemplo__nome_do_objetivo__greet_flow.run_config = KubernetesRun(image=constants.DOCKER_IMAGE.value)
