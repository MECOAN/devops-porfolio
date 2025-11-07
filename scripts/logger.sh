#!/bin/bash

# Define the timestamp format
timestamp(){
    date +"%Y-%m-%d %H:%M:%S"
}

# Function to print informational log messages
# Displays a bold blue timestamp and [INFO] tag, followed by the message in default color
log_info(){
    echo -e "\033[1;34m[$(timestamp)] [INFO]\033[0m $1" | tee -a "$LOG_FILE"
}

# Function to print warniong log messages
# Displays a bold yellow timestamp and [INFO] tag, followed by the message in default color
log_warning(){
    echo -e "\033[1;33m[$(timestamp)] [WARN]\033[0m $1" | tee -a "$LOG_FILE"
}

# Function to print success log messages
# Displays a bold green timestamp and [INFO] tag, followed by the message in default color
log_success(){
    echo -e "\033[1;32m[$(timestamp)] [SUCCESS]\033[0m $1" | tee -a "$LOG_FILE"
}

# Function to print error log messages
# Displays a bold red timestamp and [INFO] tag, followed by the message in default color
log_error(){
    echo -e "\033[1;31m[$(timestamp)] [ERROR]\033[0m $1" | tee -a "$LOG_FILE"
}
