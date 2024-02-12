# Containers vs VMs
Containers share the OS/Kernel, while VMs build an entire system on the hypervisor. VMs are larger, slower, and have more isolation. Services inside the cluster are referenced by their hostname.

## Docker
- Multiple containers of the same type can be run with a Load Balancer (LB) in front of them.
- **Image**: Used to make a container.
- **Dockerfile**: Instructions to run/configure the container.
- **Container**: The systems that run and users interact with.

## Container Orchestration: Kubernetes (Google Product)
Manages containers by:
- Scaling up/down the number of containers as needed.
- Managing connectivity between containers.
- Auto-deploying.
- Making things High Availability (HA).
- Load balancing (LB) across hosts.
- And more.

## Kubernetes Architecture
- **Node**: A single machine where Kubernetes is installed and containers run.
- **Cluster**: A set of nodes that share the load between them.
- **Master**: A node in the cluster that manages other nodes, monitoring load, health, etc.

## Components of Kubernetes
- **API Server**: The front end for Kubernetes that interfaces with CLI, web pages, etc.
- **etcd**: A key-value store to manage cluster data.
- **kubelet**: Runs on each node, ensuring containers are running as expected.
- **Container Runtime**: Software that runs containers (like Docker).
- **Controller**: Monitors health of nodes, controllers, endpoints, and can add new containers if nodes break.
- **Scheduler**: Distributes work/load across nodes.

## Hierarchy
- **Deployments**: Contain ReplicaSets.
- **ReplicaSets**: Contain pods.
- **Pods**: Contain the containers (the apps).

## Master vs Worker Nodes
- **Master Node**:
  - Has `kube-api-server`.
  - Contains `etcd`.
  - Manages the scheduler.
- **Worker Node**:
  - Contains `kubelet` that interacts with the master's `kube-api-server`.

## Kubectl
The Kubernetes CLI that deploys/manages applications.
- Deploy an app: `kubectl run hello-minikube`.
- Get cluster info: `kubectl cluster-info`.
- List cluster nodes: `kubectl get nodes`.

## Pods
- A single instance of an application, which may consist of one or more containers.
- The smallest object in Kubernetes.
- Scale by adding/removing pods.

## Kubernetes YAML Files
Contain root/required values of:
- **apiVersion**: Kubernetes API version.
- **kind**.
- **metadata**.
- **spec**.

## File Types
- **ReplicationController**: Basic pod replication and lifecycle management.
- **ReplicaSet**: Advanced pod replication with expressive pod selectors.
- **Deployment**: High-level management of ReplicaSets, updates, and rollbacks.

## Replication Controller and Replica Set
- Runs multiple pods of your app.
- Brings up new pods if a pod fails.
- Does load balancing and scaling.
- Monitors existing pods.
- Ensures a specified number of pods are always running.

## Labels and Selectors
- Used by ReplicaSets to monitor pods.
- Super important for ReplicaSets to understand pods: too many pods with the same label will be pruned.

## Deployments/Upgrades
### Deployment Strategies
- **Recreate**: Kills everything, then brings up new stuff. Downside: downtime.
- **Rolling Update**: Default method that updates one pod at a time.

Allows for:
- Rolling updates.
- Rolling back changes.
- Rolling out many changes simultaneously.

### Under the Hood Upgrades
- Starts a new ReplicaSet.
- The new ReplicaSet takes down old pods and brings up new ones incrementally.
- Rollback reverses the process, bringing the old ReplicaSet back.

## Kubernetes Networking
- Nodes have a normal IP address.
- Pods have their own IP range within the cluster.
- Pods can talk to each other without Network Address Translation (NAT).
- Services listen on ports and forward requests to pods.

## Services
Connect applications together and to users:
- Users access front-end applications through services.
- Front-end accesses back-end through services.
- Back-end accesses databases through services.

### Service Types
- **NodePort**: Forwards external requests to pods.
- **Cluster IP**: Creates a virtual IP inside the cluster for service-to-service communication.
- **LoadBalancer**: Used mainly for cloud environments, providing a single URL for customers.

## Microservices
- In Docker, containers that need to communicate use the `--link` flag, e.g., `docker run --link redis:redis voting-app`, which allows the voting-app to communicate with the redis container.
