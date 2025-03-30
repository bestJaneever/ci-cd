# Base image: Jenkins with latest version
FROM jenkins/jenkins:latest

# Switch to root to install system dependencies and Python
USER root

# Update package list and install Python3, pip, and other tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    && apt-get clean

# Upgrade pip and install necessary global Python packages
RUN python3 -m pip install --upgrade pip --break-system-packages

# (Optional) Install Python development tools globally if needed
# Uncomment the line below to include additional libraries like pytest or flask
RUN python3 -m pip install pytest --break-system-packages

# (Optional) Add Python dependencies from requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt --break-system-packages

# Add environment variables to Jenkins user
ENV PATH="/var/jenkins_home/.local/bin:$PATH"

# Switch back to Jenkins user
USER jenkins

# Set Jenkins home directory as the working directory
WORKDIR /var/jenkins_home

