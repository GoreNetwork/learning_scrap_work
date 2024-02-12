# Kubernetes YAML Configuration Essentials

## Root Values
- `apiVersion`
- `kind`
- `metadata`
- `spec`

## apiVersion
Determines the API version for the resource based on its kind.

- **POD**: `v1`
- **Service**: `v1`
- **ReplicaSet**: `apps/v1`
- **Deployment**: `apps/v1`

## kind
Refer to the "kinds" listed in the `apiVersion` section for what to specify.

## metadata
Information about the Kubernetes object:
- `name`: The name of the object.
- `labels`: A dictionary allowing any key-value pairs to be set for organizational purposes.

## spec
A dictionary containing the technical specifications for the pod.

### Super Basic Pod Definition YAML File
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
    tier: frontend
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
```
apiVersion: Here, it is v1.

kind: Specifies that this is a Pod.

metadata: Includes the pod's name and labels for identification and organization.

spec: Describes the desired state of the pod, such as containers included, their names, images used, and exposed ports.

<h1>Replication Controller</h1>
Manages the specified number of pod instances.

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx-controller
spec:
  replicas: 3  # Indicates that 3 pods will be created
  selector:
    app: nginx
  template:  # Template for creating pods
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```
<h1>Replicaset</h1>
Similar to a Replication Controller but with additional labeling capabilities for more complex selection criteria.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
  labels:
    app: mywebsite
    tier: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx_app_label  # Labels must match those in the template
  template:
    metadata:
      labels:
        app: nginx_app_label
    spec:
      containers:
      - name: nginx
        image: nginx
```
<h1>Deployment</h1>



<h1>Services</h1>

<h2>NodePort Service</h2>
Exposes a service on each Node’s IP at a static port.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30008
  selector:
    app: my-app  # Label of the pod to be exposed
```
<h2>Cluster-IP Service</h2>
Provides a service inside the cluster that other services can use.


```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: ClusterIP
  selector:
    app: my-app  # Labels used for selection
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```
<h2>Load Balancer Service</h2>
Offers a LoadBalancer for services in supported cloud platforms, directing external traffic to the backend services.

Loadbalancer Service (supported cloud platforms only)


```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: LoadBalancer
  selector:
    app: my-app  # Labels used for selection
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

```
