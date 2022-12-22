# Flask-app-with-Kubernetes


Integrating kubernetes with flask and you can do similarly with django and node application also. In this integration we create docker container, pushed into your personal docker-hub account and we gonna use that image in Kuberenetes.

1. Install [minikube](https://minikube.sigs.k8s.io/docs/start/)  and [kubectl](https://kubernetes.io/docs/tasks/tools/)
2. minikube start
3. kubectl apply -f [file_name]
4. kubectl get deployment # List deployments
5. kubectl get services # List Services
6. kubectl get nodes # List all nodes
