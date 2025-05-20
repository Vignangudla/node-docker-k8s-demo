# Node Docker K8s Demo 
A sample Node.js application demonstrating Docker, Kubernetes, and GitHub Actions for CI/CD. 
 
## Setup 
- Clone the repo: `git clone https://github.com/Vignangudla/node-docker-k8s-demo.git` 
- Build Docker image: `docker build -t vignangudla/demo-app .` 
- Apply Kubernetes manifests: `kubectl apply -f kubernetes/` 
 
## CI/CD 
- CI: Builds and tests on push/PR to main or feature branches. 
- CD: Deploys to Docker Hub on tagged releases (v*.*.*). 
