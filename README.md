# SPTS Recruitment Task

This repository contains a sample Python backend app, and a series of instructions, tasks, and requirements that aim to test your DevOps skills. It's aimed to follow a real-world scenario that you might encounter in your everyday work here.

## Guidelines

Although the repository is hosted on GitHub, it is expected that the solution, including the required CI/CD automation, must be hosted on GitLab and use GitLab CI/CD.

1. Clone this repository to your local machine.
2. Create a new private repository on your GitLab profile (create a GitLab account if you don't already have one).
   - Name the repository `cloud-engineer-spts-solution-october-2025`.
3. Implement all the tasks described below, and push to a `main` branch before submitting your results.
4. Add as direct members the users we mentioned in a separate email, with at least the `Maintainer` role, to your submission repository. They will be rating your submission.

TIP: You might need to modify some aspects of the `app` itself (i.e., add missing configuration settings), but no **significant** changes should be required. You **must not** change `main` git history as well.

## Scenarios to Implement

1. Under the `app` directory, you can find a FastAPI backend service, with `poetry` to manage its dependencies. Your task is to containerize said application.
   - Prepare `docker/backend.dockerfile` that follows best practices when it comes to image size and security.
   - The final container should expose both available entrypoints, and depending on the configuration environment flag `DEVELOPMENT=[true|false]`, switch between the two.
   - In order for the `app` container to be healthy, it needs a connection to an empty PostgreSQL database; assume the supported version is `16.8`.
   - Tip: Some of the Python dependencies might require container-level dependencies to be present; make sure to provide them in a final layer.

2. Based on #1 app containerization, create `deployment/sandbox.yaml` and `deployment/production.yaml` that will serve as an MVP of **production deployment** of the app using Docker Compose (community edition). Your assumptions:
   - Follow best practices when it comes to securing `services`, `volumes`, and `network` setup.
   - Assume the host is an Ubuntu 24.04 machine with 2 vCPUs and 4 GB of RAM, and Docker is installed following the official `docker.com` APT installation guide (https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository).
   - Nginx (version 1.29.1) should be used as a reverse proxy, and it must be the only exposed service in our compositions.
     - Prepare a separate `docker/nginx.dockerfile` with its required configuration.
     - The backend app should be available under the `api/v1/` path prefix.
     - `static-content/index.html` should be made available under the `content/` path prefix.
   - `sandbox.yaml` compose should be able to run on a developer machine, without any special authorization (i.e., GitLab Image Registry), and it should be able to serve the application backend, and auto-generated swagger under `api/v1/docs`.
   - `production.yaml` compose should pull images from the internal registry hosted on GitLab CI linked with the project, do not expose `OpenAPI` docs `api/v1/docs` and follow more strict security best practices.
   - Add a backend-app service health check that does an HTTP GET on `api/v1/activity` to see if the application is healthy, and waits until it is.

3. Prepare a basic CI/CD workflow (or workflows) based on GitLab CI that will:
   - Include a CI job that lists outdated dependencies in the app project.
   - Include a CI job that tests if `docker compose up` can be run for both of the `deployment/*.yaml` compositions.
   - Re-build the `backend.dockerfile` image if either the app source code, `dockerfile`, or app dependencies change, and push the container image to the project's internal `Container Registry` (after merging/pushing to `main`).
   - Re-build the `nginx.dockerfile` if either the nginx config or `dockerfile` definition, or `index.html` changes, and push the container image to the project's internal `Container Registry` (after merging/pushing to `main`).

4. (Optional) Using <https://github.com/mingrammer/diagrams>, create `docs/gcp.py` that will **create an example infrastructure diagram** that could deploy the above application using build artifacts and `production.yaml`, and make the services exposed by the nginx reverse proxy available via HTTPS.
   - Use only basic services that you are familiar with. The simpler the infrastructure, the better! Keep in mind that it still needs to meet basic security checks (TLS, firewall, public access, etc.)!
