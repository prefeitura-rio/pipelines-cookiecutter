# Pipelines cookiecutter

Este é um template para criação de repositórios de pipelines de dados.

## Requisitos

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
- [poetry](https://python-poetry.org/docs/#installation)

## Como usar

- Use o cookiecutter para criar um repositório a partir deste template:

```bash
cookiecutter https://github.com/prefeitura-rio/pipelines-cookiecutter.git
```

- Siga as instruções do cookiecutter (exemplo abaixo):

```
$ cookiecutter https://github.com/prefeitura-rio/pipelines-cookiecutter.git
  [1/8] project_name (rj-orgao): rj-sigla-do-seu-orgao
  [2/8] project_slug (rj_sigla_do_seu_orgao):
  [3/8] gcp_project_id (rj-orgao): id-do-seu-projeto-no-gcp
  [4/8] github_default_assignee (): usuario-do-github-para-receber-notificacoes-de-issues
  [5/8] gcs_flows_bucket (rj-orgao-flows): nome-de-bucket-do-gcs-para-armazenar-flows
  [6/8] prefeitura_rio_package_version (1.0.0rc1):
  [7/8] dbt_bigquery_package_version (^1.6.1):
```

- Após o cookiecutter terminar de criar o repositório, entre na pasta criada e inicialize o git:

```bash
cd pipelines_rj_sigla_do_seu_orgao/
git init -b main
```

- Instale as dependências do projeto e configure o hook de pre-commit:

```bash
poetry install --with dev --with ci
poetry run pre-commit install
```

- Faça o primeiro commit:

```bash
git add .
git commit -m "initial commit"
```

- Crie um repositório vazio no GitHub e adicione-o como remote:

```bash
git remote add origin https://github.com/prefeitura-rio/pipelines_rj_sigla_do_seu_orgao.git
```

- Configure os seguintes secrets para o GitHub Actions:

  - `GCP_PROJECT_ID`: ID do projeto no GCP onde os flows serão deployados
  - `GCP_SA_KEY`: chave de uma conta de serviço no GCP que será utilizada para fazer o deployment dos flows. Deve estar codificada em base64.
  - `PREFECT__CLOUD__API`: URL da API do Prefect
  - `PREFECT__CLOUD__PORT`: porta da API do Prefect
  - `PREFECT__SERVER__PROJECT__PROD`: nome do projeto de produção no Prefect
  - `PREFECT__SERVER__PROJECT__STAGING`: nome do projeto de staging no Prefect
  - `PREFECT_AUTH_TOML`: arquivo de configuração de autenticação do Prefect. Deve estar codificado em base64.

- Faça o primeiro push:

```bash
git push -u origin main
```

- (Opcional, mas recomendado) Crie um arquivo de licença e adicione-o ao repositório.