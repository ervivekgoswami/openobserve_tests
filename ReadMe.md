# OpenObserve Setup & Test Framework Guide

## 📦 Application Setup

1. **Pull the Docker image and run the container**

   ```bash
      docker run -d \
      --name openobserve \
      -v $PWD/data:/data \
      -p 5080:5080 \
      -e ZO_ROOT_USER_EMAIL="root@example.com" \
      -e ZO_ROOT_USER_PASSWORD="Complexpass#123" \
       public.ecr.aws/zinclabs/openobserve:latest

2. **Start the Docker container (Windows example)**
    ```bash
       docker run -d --name openobserve
       -v "%cd%/data"
       -p 5080:5080
       -e ZO_ROOT_USER_EMAIL="ervivekgoswami@gmail.com"
       -e ZO_ROOT_USER_PASSWORD="Complexpass#123" public.ecr.aws/zinclabs/openobserve:latest
   
3. **Access the application**
    - Open your web browser and navigate to `http://localhost:5080`

4. **Load data into OpenObserve locally**
    ```powershell
    Invoke-WebRequest -Uri https://raw.githubusercontent.com/openobserve/agents/main/windows/install.ps1 
   -OutFile install.ps1 ; .\install.ps1 
   -URL http://localhost:5080/api/default/ 
   -AUTH_KEY ZXJ2aXZla2dvc3dhbWlAZ21haWwuY29tOnZlM3RwWHZyaGVRd1plVzg=

5. **Login to OpenObserve**
    - Navigate again to 👉 http://localhost:5080/
    - Login using:
    - Email: ZO_ROOT_USER_EMAIL
    - Password: ZO_ROOT_USER_PASSWORD

## ⚙️ Framework Setup

1. **Install Dependencies**
    - Navigate to the project directory.
    - Install all dependencies:
    - ```bash
      pip install -r requirements.txt
      ```
2. **Pytest - Running Tests**
    - To run all tests in headless mode:
      ```bash
      pytest
      ```
    - To run a specific test:
      ```bash
      pytest -k <test_name>

