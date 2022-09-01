# `Setup`
  ## Normal
    - Requirements
      - Python,pip
      - Install VirtualEnv
      - Activate Environment
    - After all these steps install requirement.txt file
      - pip install -r requirements.txt

    - `Running the web app`
      - python manage.py runserver
        - go to browser and type(127.0.0.1:8000)
    `If not scheduling follow the link below`
      - `https://cronitor.io/cron-reference/no-mta-installed-discarding-output`
  
  ## Docker 
    - Requirements
      - Install Docker
      - Install Docker compose
    - Building Image
      - docker build -t dj .
      - docker-compose up(to run app with docker compose)
      - docker run -p 8000:8000 dj (To run directly from app)
      - go to browser and type(http://0.0.0.0:8000/)
