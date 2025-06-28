Invoke-Expression ((& minikube docker-env) -join "`n")
docker build -t mydemoapp:v3 .
kubectl set image deployment/mydemoapp mydemoapp=mydemoapp:v3
kubectl rollout status deployment/mydemoapp
