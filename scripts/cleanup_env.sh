#!/bin/bash
# cleanup_env.sh
# Remove temporary or generated files, keeping logs and reports for debugging

# Load logger configuration
source scripts/log_config.sh
source scripts/logger.sh

log_info "Strarting environment cleanup"

# Python
if [ ! -d "venv" ] && [ ! -d "__pycache__" ];
then
    log_warning "Nothing to clean for python"
    exit 0
fi

# Deactivate python virtual environment
if [ -n "${VIRTUAL_ENV}" ];
then
    deactivate
    log_info "Virtual environment deactivated before cleanup"
fi

# Remove python virtual environment
if [ -d "venv" ];
then
    rm -rf venv
    log_success "Python virtual environment directory removed"
fi

# Remove compiled python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
log_success "Removed Python cache files"

# Remove temporary buid/test artifacts
TEMP_DIRS=("build" "dist" ".pytest_cache" ".mypy_cache")
for dir in "${TEMP_DIRS[@]}";
do
    if [ -d "${dir}" ];
    then
        rm -rf "${dir}"
        log_success "Removed ${dir} directory"
    fi
done

log_info "Finishing environment cleanup"
