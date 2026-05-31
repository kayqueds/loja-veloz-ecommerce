# Relatório Técnico — Loja Veloz

## Resumo executivo

Este relatório documenta a solução de microsserviços para a Loja Veloz e as decisões de infraestrutura e DevOps adotadas para garantir velocidade, automação, rastreabilidade e segurança.

## 1. Teoria: Arquitetura de Microsserviços e papel do DevOps

- Arquitetura de microsserviços: cada serviço (pedidos, pagamentos, estoque, api-gateway, api-services) é implementado e implantado independentemente, reduzindo acoplamento e acelerando entregas.
- Papel do DevOps: prover pipelines de CI/CD, automação de builds e deploys, infraestrutura como código (Kubernetes manifests), e observabilidade (métricas, logs, traces) para permitir entregas rápidas e seguras.

## 2. Docker vs Kubernetes

- Docker: empacotamento de cada serviço em imagem imutável, contendo runtime e dependências (útil para desenvolvimento e distribuição).
- Kubernetes: orquestração das imagens em um cluster, fornecendo escala, descoberta de serviços, load balancing, health checks e estratégias de deploy (RollingUpdate, Canary, etc.).

## 3. Justificativas das escolhas

- Por que Kubernetes? Permite escalabilidade horizontal, tolerância a falhas, gerenciamento de configuração/segredos, e políticas de rollout controladas.
- Por que RollingUpdate? Minimiza downtime durante deploys, atualizando réplicas gradualmente e mantendo disponibilidade para a aplicação de pedidos em produção.

## 4. Observabilidade

- Métricas: coletores Prometheus expõem métricas dos serviços; Grafana exibe Dashboards para SLOs e alertas.
- Logs: centralização via EFK (Elasticsearch/Fluentd/Kibana) para correlação de eventos entre serviços.
- Tracing: OpenTelemetry + Jaeger para rastrear chamadas distribuídas (útil para diagnosticar latência entre `api-gateway` e serviços).

## 5. Segurança

- `securityContext` aplicado nos `Deployments` para evitar execução como root (`runAsNonRoot`, `runAsUser`, `fsGroup`) e desabilitar `allowPrivilegeEscalation`.
- Segredos armazenados em `Secret` (codificados em base64) e configurações em `ConfigMap`. Jenkins/GitHub Actions devem consumir secrets via GitHub Secrets.

## 6. Implantação e pipeline

- Uso de `docker build` para gerar imagens, e `kubectl apply -f k8s/` para aplicar manifestos.
- Pipeline GitHub Actions criado em `.github/workflows/main.yml` para testes, build e push das imagens para Docker Hub.

## 7. Como gerar PDF

Instale o `pandoc` e execute:

```bash
pandoc REPORT.md -o REPORT.pdf --pdf-engine=xelatex
```

> Observação: lembrar de substituir valores sensíveis no `k8s/config-secrets.yaml` por segredos reais antes de aplicar no cluster.
