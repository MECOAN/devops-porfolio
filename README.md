# DevOps Portfolio - CI/CD Simulation

## General Description
The main objective of this proyect is to build a complete continuous integration(CI) and continuous delivery(CD) pipeline, using Bash, Python, Java and C.
Each langua has its own set of automated tests, which are executed both in a local environment and inside Docker container

## Project structure
/src/python/  -> Python source code
/src/java/    -> Java source code
/src/c/       -> C source code
/test/python/ -> Python tests with pytest
/test/java/   -> Java tests with JUnit
/test/c/      -> C tests with CUnit
/scripts/     -> Bash scripts for the pipeline

## Bash scripts Description
logger.sh       -> Defines the format and color of the log output
log_config.sh   -> Creates the log directory and prepare the log file
setup_env.sh    -> Install all required dependencies in the environment to run the python tests
run_tests.sh    -> Execute all the python tests using pytest, generate the report and logs results
cleanup_env.sh  -> Removes the python virtual environment and all th temporary files (keeping logs and reports)
cleanup_logs.sh -> Deletes all the logs and report files
build_all.sh    -> Run all the bash scripts (cleanup_logs -> setup_env -> run_tests -> cleanup_env)

## Pipeline flow
build_all.sh
  - cleanup_logs.sh
  - setup_env.sh
  - run_tests.sh
  - cleanup_env.sh

## Manual excution
Python:
    bash cleanup_logs.sh
    bash setup_env.sh
    bash run_tests.sh
    bash cleanup_env.sh

Requirements
    - Linux environment
    - Python 3.12+
    - Bash 5.0+
    - Installed packages:
        - python3-venv
        - python3-pip

## Docket
To be implemented
