# OTP Generator Project

## Table of Contents

- [Overview](#overview)

- [Installation](#installation)

- [Prerequisites](#prerequisites)

- [Clone the Repository](#clone-the-repository)

- [Create and Activate a Virtual Environment](#create-and-activate-a-virtual-environment)

- [Install Dependencies](#install-dependencies)

- [Usage](#usage)

- [Using Docker](#using-docker)

## Overview

Explain briefly what your FastAPI project does and its main features.

### Clone the Repository

```bash

git  clone  https://github.com/your-username/your-fastapi-project.git

cd  your-fastapi-project

```

## Installation

Create and Activate a Virtual Environment

```bash
python -m venv venv
```

source venv/bin/activate # On Windows, use `venv\Scripts\activate`

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Usage

Run the FastAPI App Locally

```bash
uvicorn main:app --reload
```

Visit http://127.0.0.1:8000/ in your browser to access the API documentation.

### Using Docker

Build the Docker image:

```bash
docker build -t you-fastapi-app
```

Run the Docker container:

```bash
docker run -d -p 8000:80 --name your-fastapi-container your-fastapi-app
```

### Prerequisites

Ensure you have the following installed on your system:

- [Python](https://www.python.org/downloads/)

- [Docker](https://www.docker.com/get-started)

### Reference

https://codevoweb.com/two-factor-authentication-2fa-in-fastapi-and-python/
