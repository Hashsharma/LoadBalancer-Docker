# LoadBalancer-Docker
Load Balancer Docker


## 🐳 Running the Application with Docker

### Build the Docker Image

```bash
docker build -t fastapi-app .
```

This command builds the Docker image using the `Dockerfile` in the current directory and tags it as `fastapi-app`.

---

### Run the Docker Container

```bash
docker run -d \
  --name fastapi-container \
  -p 8000:8000 \
  fastapi-app
```

**Command options explained:**

* `-d`
  Runs the container in detached (background) mode.

  > Remove `-d` to run the container in the foreground and see logs live.

* `--name fastapi-container`
  Assigns a custom name to the container for easier management.

* `-p 8000:8000`
  Maps port `8000` on the host machine to port `8000` inside the container.

* `fastapi-app`
  The name of the Docker image to run.

---

### Access the Application

* API: `http://localhost:8000`

---

### View Logs

```bash
docker logs -f fastapi-container
```

This command streams the container logs in real time.

---

### Stop the Container

```bash
docker stop fastapi-container
```

---

### Remove the Container

```bash
docker rm fastapi-container
```

---