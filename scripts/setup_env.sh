#!/bin/bash
# setup_env.sh
# Prepate environment for local testing

# Create the folder and file for logs
source scripts/log_config.sh
# Get the format logger messages functions
source scripts/logger.sh

log_info "Setup Environment start"

# Verify if python is installed
if ! command -v python3 &> /dev/null; 
then
    log_error "python3 was not found, the python tests wouldnt be executed"
else
    # Create the visrtual environment
    log_info "Creating virtual environment (venv)"
    python3 -m venv venv || log_error "Failed to activate venv"

    #Activate the environment
    source venv/bin/activate || log_error "Failed to activate venv"

    # Upgrading pip and install dependencies
    log_info "Installing dependencies"
    pip install --upgrade pip
    if [ -f "requirements.txt" ];
    then
        pip install -r requirements.txt || log_error "Failed to sintall dependencies"
    else
        log_info "No requirements.txt foud, installing pytest only"
        pip install pytest pytest-html || log_error "Failed to install pytest"
    fi

    # Verify pytest
    if [ ! command -v pytest $> /dev/null ];
    then
        log_error "Pytest not found after installation"
    fi

    # Prepare reports directory
    mkdir -p reports
fi

log_info "Setup Environment end"
