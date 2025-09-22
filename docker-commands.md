```bash
docker build -f .\DockerFile -t pyapp .
docker run -it pyapp
```

### For tag with my user name. the tag latest can be changed to a specific version.
docker build -f .\DockerFile -t carlosvargas91/ai-py-app-test:latest .
docker push carlosvargas91/ai-py-app-test:latest

### docker python is running on port 8000, so we need to map the port 8000 to the port 8000 of the host.
docker run -it -p 8000:8000 pyapp

### To see inside the container
docker exec -it <container_id> bash

### compose yaml
docker compose up # To run the app
docker compose down # Downs the container
docker compose build

### To compose up and build
docker compose up --build

### To run as bash terminal
docker compose run app /bin/bash

### watch mode
docker compose up --watch

### To remove the volumes
docker compose down -v

### Docker model runner
_From host terminal_
```bash
curl http://localhost:12434/engines/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/gemma3",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
```

_From within a container_
```bash
curl http://model-runner.docker.internal/engines/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/gemma3",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
```

### First ai iteration
llm_base.invoke("What is your name?")


### Python commands
python -i myscript.py # Runs the script interactive