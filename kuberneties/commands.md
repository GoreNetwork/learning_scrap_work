# Crossover Useful Commands

## General Commands
- Get all deployments, ReplicaSets (RS), and Pods: `KC get all`

## Pod Commands
- Deploy an application (in a pod): `kubectl run hello-minikube`
  - Example for nginx: `kubectl run nginx --image nginx`
    - Note: Pod name can be any string.
- Get cluster information: `kubectl cluster-info`
- List cluster nodes: `kubectl get nodes`
- Show pods: `kubectl get pods`
  - Displays:
    - Pod name
    - Number of containers
    - Status
    - Number of restarts
    - Age
  - Tip: Use `-o wide` to get node name and IP of pod.
- Describe a pod: `kubectl describe pod [pod_name]`
  - Provides detailed information similar to `docker inspect`.
- Create a pod from a YAML file: `kubectl apply -f pod_file_name.yml`
  - This also applies any changes made to the YAML file to the pod.
- Describe a node: `kubectl describe node [node name]`
- Generate a YAML file without executing the command: `kubectl run redis --image=redis123 --dry-run=client -o yaml > [pod_name].yml`
- Delete a pod: `kubectl delete pod [pod_name]`

## ReplicaSet/ReplicationController Commands
- Create a ReplicaSet/ReplicationController: `kubectl create -f [yml file name]`
- List ReplicaSets: `kubectl get replicaset`
- List ReplicationControllers: `kubectl get replicationcontroller`
- Scale a ReplicaSet: `kubectl scale rs [app_name] --replicas=2`
- Describe a ReplicaSet: `kubectl describe rs [app-name]`
- Delete a ReplicaSet and its associated pods: `kubectl delete rs app_name`

## Updating Running ReplicaSets
- Replace a ReplicaSet: `kubectl replace -f [replicaset file name]`
- Update the running ReplicaSet (not the file): `kubectl scale --[name of value]=[new value] -f [name of replicaset file]`
  - Example: `kubectl scale --replicas=6 -f replicaset_nginx.yml`
- Scale a ReplicaSet directly: `kubectl scale --[name of value]=[new value] [type] [name]`
  - Example: `kubectl scale --replicas=6 replicaset phantom_nginx_app`
- Edit a ReplicaSet configuration: `kubectl edit rs [app-name]`

## Deployment Commands
- Create a deployment: `kubectl create -f [deployment-filename]`
  - Use `--record` to annotate the change.
- Delete a deployment: `kubectl delete deployment [deployment name]`
- List deployments: `kubectl get deployments`
- Describe a deployment: `kubectl describe deployment [deployment_name]`
- Create a deployment with specifics: `kubectl create deployment [deployment_name] --image=[image to use] --replicas=[#]`
- Check rollout status: `kubectl rollout status deployment/[app-name]`
- View rollout history: `kubectl rollout history deployment/[app-name]`
- Apply changes from a file: `kubectl apply -f [deployment-file-name]`
- Set a specific container image in a deployment: `kubectl set deployment/[app-name] nginx-container=nginx:191`
  - Warning: This updates the deployment but not the configuration file.
- Undo a deployment rollout: `kubectl rollout undo deployment/[app-name]`

## Service Commands
- Create a service: `kubectl create -f [service-definition-file]`
- List services: `kubectl get services`
