#!/bin/bash
# Declare the log dir and file to use

LOG_DIR="./logs"
mkdir -p "${LOG_DIR}"
RUN_ID=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${LOG_DIR}/setup_env_${RUN_ID}.log"
export LOG_FILE
