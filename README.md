# 🧠💰 Financial AI Agent — Powered by Agno

Um agente financeiro inteligente desenvolvido com **Agno**, capaz de consultar automaticamente **SELIC, CDI, IPCA**, realizar simulações de investimentos e responder perguntas financeiras em linguagem natural.

Este projeto foi criado para servir como uma automação financeira conectada à API do Banco Central e ferramentas personalizadas.

---

## 🚀 Funcionalidades Principais

### 🔹 **Consulta automática de indicadores econômicos**

* SELIC (série SGS 432)
* CDI (série SGS 12)
* IPCA (série SGS 433 ou fornecido manualmente)
* Conversão de taxas diárias, mensais e anuais

### 🔹 **Cálculos e simulações financeiras**

* Rentabilidade com aportes mensais
* Juros compostos
* Correção monetária pelo IPCA
* Simulações de investimentos em:

  * Tesouro Selic
  * CDB atrelado ao CDI
  * Correção via IPCA

### 🔹 **Ferramentas customizadas (Tools)**

O projeto utiliza *tools* do Agno para:

* Obter SELIC direto do BCB
* Obter CDI direto do BCB
* Corrigir valores pelo IPCA
* Calcular rentabilidades reais e nominais

### 🔹 **Agente conversacional inteligente**

* Conversa natural com o usuário
* Explica cálculos passo a passo
* Sugere simulações
* Analisa cenários
* Formata respostas com clareza e objetividade

---

## 🧩 Estrutura das Tools

### ✔️ **SELIC Tool**

Busca a taxa diretamente na API do Banco Central e trata cenários sem retorno.

### ✔️ **CDI Tool**

Consulta a série 12 do BCB e converte para taxa diária (252 dias úteis) para simulações.

### ✔️ **IPCA Tool**

Correção monetária baseada em taxa anual informada pelo usuário.

### ✔️ **Simulações**

Combinam aportes + taxas para resultados precisos.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Agno** (framework para agentes de IA)
* **Requests** (consultas ao BCB)
* **Banco Central do Brasil (SGS API)**
* **Ferramentas customizadas em Python**

---

## 📦 Instalação

```bash
git clone https://github.com/seu-repo/finance-ai-agent.git
cd finance-ai-agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Como Rodar

```bash
streamlit run app.py
```

O agente será iniciado e pronto para responder com dados financeiros reais.

---

## 🧠 Exemplo de Uso

**Pergunta:**

```
Quero investir 1000 reais por mês durante 12 meses. Quanto terei no final pelo Tesouro SELIC, CDI e IPCA?
```

**Resposta do Agente (exemplo):**

* Tesouro Selic: R$ 12.728,00
* CDI: R$ R$ 12.630,00
* IPCA: R$ R$ 12.310,00

---

## 📈 Objetivo do Projeto

Criar uma solução simples, direta e poderosa que permita qualquer pessoa simular investimentos e consultar indicadores econômicos com conversas naturais.

---

## 🤝 Contribuição

Pull requests são bem-vindos! Se quiser contribuir:

```bash
git checkout -b minha-feature
# faça suas alterações
git add .
git commit -m "feat: adiciona nova funcionalidade"
git push origin minha-feature
```

---

## Observação Importante

Para segurança dos dados, o arquivo .env foi removido. 
Caso faça o git clone do projeto, adicione o arquivo com as seguintes informações:
SECRET_KEY=(Sua SecretKey)
PYTHONPATH=
OPENAI_API_KEY=(Sua chave)

## 📜 Licença

Este projeto está sob a licença MIT.

---

## 💬 Contato

Se quiser expandir este agente ou criar um dashboard visual avançado, estou pronto para ajudar!
# AGNO-FinanceAgent
