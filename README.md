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


### Architecture Diagram

```
Client Request
      │
      ▼
   Port 80
  (Load Balancer)
      │
      ▼
+-----------------------+
|  Nginx (Load Balancer)|
|   container            |
+-----------------------+
      │
      ▼
 Distributes requests to:
      │
      ├─> app1:8000 (container port, internal only)
      ├─> app2:8000 (container port, internal only)
      └─> app3:8000 (container port, internal only)
```

### How It Works

1. **Client requests** are sent to port 80 on the host machine.
2. Requests hit the **Nginx load balancer container**, which distributes traffic evenly across the `user_service` application containers.
3. Each `user_service` container runs **FastAPI** on port `8000`, but this port is **not exposed to the host** — it is only accessible internally within the Docker network.
4. Nginx handles routing, ensuring:

   * Load balancing across multiple instances
   * High availability
   * Centralized entry point

---

### Docker Network Notes

* All containers share a **custom Docker network** for internal communication.
* No container ports are exposed to the host, except for the Nginx load balancer (port 80).
* This setup allows **scaling services independently**.

---

### Benefits

* 🔹 **Scalable**: Add more `user_service` containers without changing the host configuration.
* 🔹 **Secure**: Internal services are not exposed publicly.
* 🔹 **Maintainable**: Each service runs independently in its own container.

---

```text
Your Machine / Host
+----------------------------------+
|                                  |
|  Docker Engine                   |
|  +----------------------------+  |
|  | Container: fastapi_container | <-- Container name
|  |  +-----------------------+  |
|  |  | Image: fastapi_image  |  <-- Image name
|  |  |  +-----------------+ |  |
|  |  |  | FastAPI App     | |  | <-- App inside container (main:app)
|  |  |  | my_fastapi_app/ | |  |
|  |  |  +-----------------+ |  |
|  |  +-----------------------+  |
|  +----------------------------+  |
|                                  |
+----------------------------------+
```
8001:8000
HOST_PORT (first 8001) → the port on your local machine (your laptop/desktop) that you will use to access the app.

CONTAINER_PORT (second 8000) → the port inside the Docker container where your app is running.



---

# FastAPI Docker Setup with Nginx Load Balancer

This project runs multiple **FastAPI** containers and uses **Nginx** as a load balancer using Docker.

## Setup Instructions

### 1. Create a Docker Network

Create a custom network so containers can communicate:

```bash
docker network create my-network
```

### 2. Run FastAPI Containers

Run two instances of the FastAPI app on the network:

```bash
docker run -d --name fastapi-container --network my-network fastapi-app
docker run -d --name fastapi-container2 --network my-network fastapi-app
```

### 3. Run Nginx Load Balancer

Run Nginx to distribute traffic between the FastAPI containers:

```bash
docker run -d --name nginx-loadbalancer --network my-network -p 8080:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro nginx:latest
```

### 4. Access the Application

Open your browser and visit:

```
http://localhost:8080
```

Requests will be load balanced between the two FastAPI containers.

---

