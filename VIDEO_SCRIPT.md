Roteiro (≈4 minutos)

1. 0:00–0:30 — Introdução: Apresentar Loja Veloz e o problema (escalabilidade e disponibilidade)
2. 0:30–1:30 — Estrutura do projeto: mostrar `services/`, `k8s/`, `docker-compose.yml`
3. 1:30–2:30 — Arquitetura: explicar Docker vs Kubernetes, serviços e DB
4. 2:30–3:30 — Demo rápida: `docker compose up --build` ou mostrar `k8s/` manifests
5. 3:30–4:00 — Encerramento: benefícios e observabilidade

Roteiro detalhado (passo a passo):

0:00–0:20 — Apresentação rápida: "Sou desenvolvedor/DevOps; Loja Veloz vende online e precisa de disponibilidade e escala."

0:20–0:50 — Mostrar estrutura no VS Code: abra a árvore de arquivos, destaque `services/`, `k8s/`, `docker-compose.yml`, `README.md`.

0:50–1:40 — Arquitetura explicada: explique o papel de cada serviço (pedidos, pagamentos, estoque, api-gateway) e diferença entre Docker (imagem) e Kubernetes (orquestração).

1:40–2:40 — Demonstração curta:

- opção local: rodar `docker compose up --build` (mostre terminal)
- opção cluster: mostrar `k8s/` manifest (`kubectl apply -f k8s/`) e comentar `securityContext` e probes.

2:40–3:20 — Observabilidade e segurança: comente sobre métricas (Prometheus), logs (EFK) e tracing (Jaeger). Destaque o `securityContext` e uso de `Secret`.

3:20–4:00 — Encerramento: benefícios (escala, resiliência, deploys rápidos) e call-to-action: link no README e instruções para rodar pipeline.
