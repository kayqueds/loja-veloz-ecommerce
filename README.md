# Loja Veloz — Setup Rápido

## Sobre o Projeto
Infraestrutura de e-commerce baseada em microsserviços, focada em alta disponibilidade e escalabilidade. Projetada para suportar picos de tráfego através de orquestração com Kubernetes e automação via CI/CD.

## Demonstração (Pitch)
[Clique aqui para assistir à apresentação do projeto](LINK_DO_TEU_VIDEO_AQUI)
Comandos principais:

- Rodar local com Docker Compose:

```
docker compose up --build
```

- Parar e remover:

```
docker compose down
```

- Aplicar manifestos no Kubernetes:

```
kubectl apply -f k8s/
```

CI/CD:

- Adicione os secrets `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN` nas GitHub Secrets.
- Push na branch `main` dispara o workflow.

Gerar PDF do relatório (opcional):

```bash
pandoc REPORT.md -o REPORT.pdf --pdf-engine=xelatex
```

Observações de segurança:

- Configure os secrets `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN` em GitHub Secrets para permitir push das imagens.
- Atualize `k8s/config-secrets.yaml` substituindo o valor base64 da senha por sua senha real codificada.

Rollout controlado (exemplo):

```bash
kubectl rollout status deployment/api-gateway
kubectl rollout restart deployment/pedidos
```
