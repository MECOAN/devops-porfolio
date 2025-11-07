#!/bin/bash
# cleanup_logs.sh
# Clean up log and report files 

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${PROJECT_ROOT}/logs"
REPORT_DIR="${PROJECT_ROOT=}/reports"

echo "PROJECT_ROOT: ${PROJECT_ROOT}"
echo "LOG_DIR: ${LOG_DIR}"
echo "REPORT_DIR: ${REPORT_DIR}"

LOG_OUTPUT=1
REPORT_OUTPUT=1

# Check if log and report directories exists
if [ -d "${LOG_DIR}" ];
then
    rm -rf "${LOG_DIR}"
    LOG_OUTPUT=$?
fi

if [ -d "${REPORT_DIR}" ];
then
    rm -rf "${REPORT_DIR}"
    REPORT_OUTPUT=$?
fi

if [ ${LOG_OUTPUT} -eq 0 ] && [ ${REPORT_OUTPUT} -eq 0 ];
then
    exit 0
else
    exit 1
fi

