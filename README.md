# MentorX AI 🤖🚀

> **Status do Projeto:** 💡 Fase de Conceção / Candidato ao Orange Summer Challenge 2026

O **MentorX AI** é uma plataforma inteligente de orientação profissional e desenvolvimento de competências desenhada para democratizar o acesso à mentoria de qualidade para jovens africanos. Através do ecossistema, ajudamos os utilizadores a descobrir caminhos de carreira, estruturar planos de estudo personalizados e alinhar competências técnicas com as exigências do mercado real.

---

## 🔥 Funcionalidades Principais

* **Assistente Inteligente Gideon:** Um agente de IA focado em mentoria de carreira que responde a dúvidas, sugere stacks de tecnologia e orienta o plano de desenvolvimento do utilizador.
* **Planos de Estudo Adaptativos:** Geração automática de roteiros (roadmaps) com metas claras baseadas nos objetivos de carreira do utilizador.
* **Métricas de Evolução:** Painel visual para acompanhar o progresso das competências digitais e empreendedoras adquiridas.

---

## 🏗️ Arquitetura Proposta do Sistema

O fluxo de dados foi desenhado para ser escalável, seguro e local:

```text
[ Utilizador ] ──(Interface Web/Mobile)──> [ Painel MentorX ]
                                                  │
                                                  ▼
                                           [ Agente Gideon ]
                                                  │
                                                  ▼
                                       [ LLM Local / Ollama ]