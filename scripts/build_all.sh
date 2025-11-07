#!/bin/bash
# build_all.sh
# Main driver for local CI/CD pipeline

source scripts/log_config.sh
source scripts/logger.sh

PIPELINE_START=$(date +"%s")

bash scripts/cleanup_logs.sh

bash scripts/setup_env.sh
if [ $? -ne 0 ];
then
    log_error "Error seting up the environment"
    exit 1
fi

bash scripts/run_tests.sh
if [ $? -eq 0 ];
then
    log_success "All the tests passed successfully"
else
    log_error "Some tests scenarios failed, verify the logs and reference files"
fi

bash scripts/cleanup_env.sh
if [ $? -ne 0 ];
then
    log_error "Problem cleaning the environment"
fi

PIPELINE_END=$(date +"%s")
DURATION=$((PIPELINE_END-PIPELINE_START))
log_info "Total time: ${DURATION} seconds"
