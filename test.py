#!/usr/bin/env python
# coding: utf-8

"""
Comprehensive test script to validate Tier 1 and Tier 2 DevOps parsers.
This script includes examples of all elements that DevOpsConceptCollector (Tier 1)
and DevOpsConceptCollectorTier2 (Tier 2) can extract.
"""

import os
import subprocess
import json
import yaml
import requests
import shutil
import glob
from github import Github  # PyGithub for GitHub API
from pathlib import Path
import logging
import argparse
import boto3
from google.cloud import storage
from azure.mgmt.compute import ComputeManagementClient
from kubernetes import client, config
from typing import Union, List, Optional

# Tier 1 & 2: Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestDevOps")

# Tier 1 & 2: Constants
API_TOKEN: str = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Hardcoded secret (Tier 1)
SERVICE_NAME = "NodeDockerK8sDemo"  # Tier 2
DEFAULT_TIMEOUT = 30  # Tier 2

# Tier 1 & 2: Environment Variable Access
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Tier 1 & 2
APP_SECRET = os.environ["APP_SECRET_KEY"]  # Tier 1 & 2
DEBUG_MODE = os.getenv("DEBUG_FLAG")  # Tier 1 & 2

# Tier 2: Variables
api_key = os.getenv("MY_API_KEY")  # Tier 2
is_production: bool = False  # Tier 2 with type annotation

# Tier 1 & 2: Special Tags and Comments
# @task initialize_project
# TODO: Refactor secret handling for better security
# FIXME: Add retry logic for HTTP requests

# Tier 2: Decorators
def log_execution(func):
    """Decorator to log function execution."""
    def wrapper(*args, **kwargs):
        logger.info(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Tier 1: Class Definition
class BasePipeline:
    """Base class for CI/CD pipelines."""
    def common_method(self):
        pass

# Tier 1 & 2: Class with Inheritance and Decorator
class K8sPipeline(BasePipeline):  # Tier 2: Inheritance
    """Pipeline for Kubernetes deployments."""
    @log_execution  # Tier 2: Decorator
    def __init__(self, token: str, name: str):  # Tier 2: Type annotations
        self.gh = Github(token)  # Tier 1: GitHub API
        self.name: str = name  # Tier 2: Type annotation
        logger.info(f"Initialized pipeline {name}")  # Tier 2: Logging

    @log_execution
    def deploy(self, image: str) -> bool:  # Tier 2: Type annotation
        """Deploys a container image to Kubernetes."""
        try:  # Tier 2: Error handling
            config.load_kube_config()  # Tier 2: Kubernetes
            v1 = client.CoreV1Api()  # Tier 2: Kubernetes
            logger.info(f"Deploying {image} to Kubernetes")  # Tier 2: Logging
            # Simulate pod listing
            # v1.list_pod_for_all_namespaces(watch=False)
            return True
        except Exception as e:  # Tier 2: Error handling
            logger.error(f"Kubernetes deployment failed: {e}")  # Tier 2: Logging
            return False

# Tier 1: Async Function
async def pull_docker_image(image: str):  # Tier 1: Async function
    """Pulls a Docker image using subprocess."""
    subprocess.run(["docker", "pull", image], check=True)  # Tier 1: Subprocess, CLI tool
    logger.info(f"Pulled Docker image {image}")  # Tier 2: Logging

# Tier 1 & 2: Function with Type Annotations and Subprocess
@log_execution  # Tier 2: Decorator
def process_config(config_path: str) -> Optional[dict]:  # Tier 2: Type annotation
    """Loads and processes a YAML configuration."""
    # Tier 1: File manipulation
    config_file = Path(".github/workflows") / config_path
    # Tier 1 & 2: YAML parsing
    if config_file.exists():
        with open(config_file, "r") as f:  # Tier 1 & 2: File manipulation
            config_data = yaml.safe_load(f)  # Tier 1 & 2: YAML parsing
            logger.debug(f"Loaded config from {config_path}")  # Tier 2: Logging
            return config_data
    return None

# Tier 1 & 2: Function with HTTP Request and Error Handling
def fetch_data(url: str) -> bool:  # Tier 2: Type annotation
    """Fetches data from a URL."""
    try:  # Tier 2: Error handling
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)  # Tier 1 & 2: HTTP request
        response.raise_for_status()
        logger.info(f"Fetched data from {url}")  # Tier 2: Logging
        if "config.yaml" in url:  # Tier 2: YAML reference
            with open("config.yaml", "w") as f:  # Tier 1 & 2: File manipulation
                json.dump(response.json(), f)  # Tier 1: JSON parsing
        return True
    except requests.exceptions.RequestException as e:  # Tier 2: Error handling
        logger.error(f"HTTP request failed: {e}")  # Tier 2: Logging
        return False
    except yaml.YAMLError as ye:  # Tier 2: Error handling
        logger.error(f"YAML parsing failed: {ye}")  # Tier 2: Logging
        return False
    finally:  # Tier 2: Error handling
        logger.debug("Fetch attempt completed")  # Tier 2: Logging

# Tier 2: Command-Line Argument Parsing
def parse_args() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Test DevOps parser")  # Tier 2: Argparse
    parser.add_argument("--image", default="nginx:latest", help="Docker image to deploy")
    parser.add_argument("--url", default="https://example.com", help="URL to fetch")
    return parser.parse_args()

# Tier 1 & 2: File Manipulation
def manage_files(source: str, dest: str) -> None:
    """Performs file operations."""
    shutil.copy(source, dest)  # Tier 1: File manipulation
    config_files = glob.glob("*.yaml")  # Tier 1: File manipulation
    os.path.join("data", "config.yaml")  # Tier 1: File manipulation
    logger.info(f"Copied {source} to {dest}")  # Tier 2: Logging

# Tier 2: Cloud SDK Usage
def setup_cloud_services() -> None:
    """Initializes cloud SDK clients."""
    # AWS
    s3_client = boto3.client("s3", region_name="us-east-1")  # Tier 2: Cloud SDK
    logger.info("Initialized AWS S3 client")  # Tier 2: Logging
    # Google Cloud
    gcp_client = storage.Client()  # Tier 2: Cloud SDK
    logger.info("Initialized GCP Storage client")  # Tier 2: Logging
    # Azure (commented out for simplicity)
    # azure_client = ComputeManagementClient(None, "dummy_sub_id")  # Tier 2: Cloud SDK

# Tier 1 & 2: Main Entry Point
if __name__ == "__main__":
    args = parse_args()  # Tier 2: Argparse
    pipeline = K8sPipeline(GITHUB_TOKEN, SERVICE_NAME)  # Tier 1: GitHub API, Tier 2: Class
    pipeline.deploy(args.image)  # Tier 2: Internal function call
    process_config("main.yml")  # Tier 1 & 2: Function call
    fetch_data(args.url)  # Tier 1 & 2: Function call
    manage_files("source.txt", "dest.txt")  # Tier 1 & 2: Function call
    setup_cloud_services()  # Tier 2: Function call
    # Simulate async call (commented out for simplicity)
    # import asyncio
    # asyncio.run(pull_docker_image(args.image))
    logger.info("Test script execution completed")  # Tier 2: Logging
