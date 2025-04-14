# Evo2 Trial

This repository demonstrates how to set up and run a simple example using the [**Evo2**](https://github.com/ArcInstitute/evo2) model with a Docker container.

## Pre-requisites

Before running the code, ensure the following hardware and software requirements are met:

### Hardware
- An NVIDIA GPU **Hopper architecture** or newer (e.g., H100, L40) is required to run Evo2 efficiently.

### Software
- [Docker](https://www.docker.com/) 
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html) (to enable GPU access inside Docker)

---

## Quick Start 

1. **Pull the Docker image**  
   Make sure you have Docker installed, then pull the required container image:

   ```bash
   docker pull warrents/evo2_trial:latest
   ```

2. Run the Docker container
   ```bash
   docker run --gpus all -it --rm \
   --shm-size 2g \
   -p 8888:8888 \
   -w /workspace/evo2 \
   warrents/evo2_trial:latest \
   ```

3. Activate the env:
   ```bash
   conda activate evo2
   ```

4. Run the Python script
   ```bash
   python trial.py
   ```

##  Reference
This project is based on the Evo2 model developed by the Arc Institute.
For more details, see the official repository:
👉 https://github.com/ArcInstitute/evo2
