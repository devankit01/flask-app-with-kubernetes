# Flask-app-with-Kubernetes

<!-- Coammands To Run -->
docker build --tag flask-docker .
docker run  -p 5000:5000 flask-docker
minikube image load flask-docker
minikube addons enable ingress
minikube tunnel
kubectl apply -f kubernetes/flask-deployment.yaml
kubectl apply -f kubernetes/flask-service.yaml
kubectl get deplyments
kubectl get service
kubectl get pods
