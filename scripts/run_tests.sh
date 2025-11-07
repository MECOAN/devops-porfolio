#!/bin/bash
# run_tests.sh
# Run Python tests using pytest and generate HTML report

# Load logging configuration
source scripts/log_config.sh
source scripts/logger.sh

log_info "Starting python test execution"

# Validate environment
if [ ! -d "venv" ]; 
then
    log_error "Python virtual environment not found"
    exit 1
fi
log_success "Python virtual environment found"

# Set active the environment
source venv/bin/activate
if [ $? -ne 0 ];
then
    log_error "Failed to activate the virtual environment"
    exit 1
fi
log_success "Python virtual environment activated"

# Validate pytest installation
if ! command -v pytest &>/dev/null;
then
    log_error "Pytest not found"
    exit 1
fi

# Prepare reports directory
REPORT_DIR="./reports"
mkdir -p "${REPORT_DIR}"
REPORT_ID=$(date +"%Y%m%d_%H%M%S")
REPORT_FILE="${REPORT_DIR}/report_${REPORT_ID}.html"

log_info "Running pytest and generating report: ${REPORT_FILE}"

# Execute tests
pytest --disable-warnings --html="$REPORT_FILE" --self-contained-html | tee -a "${LOG_FILE}"
PYTHON_TEST_EXIT_CODE=${PIPESTATUS[0]}

if [ ${PYTHON_TEST_EXIT_CODE} -eq 0 ];
then
    log_success "All Python tests passed successfully"
else
    log_error "Some tests failed. Check the report and logs for details"
fi

deactivate
log_info "Finishing python test execution"
