To deploy the app:

```
python3 cerana.py 5 https://github.com/GlennTatum/angular-py > deployment.yml
kubectl apply -f deployment.yml
```

k3d Install

```

curl -sSf https://get.k0s.sh | sudo sh

sudo k0s install controller --single

sudo k0s start # wait a minute

sudo k0s kubectl get nodes

sudo apt install git

sudo apt install python3.11-venv

curl https://releases.rancher.com/install-docker/27.5.sh | sh

# it should already be deployed

~/cerana/k8s/gitpod$ sudo docker build . -t glenntatum/opencodeserver:latest

# https://hub.docker.com/repositories/glenntatum

docker login
```

