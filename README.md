# projeto-matrizes

Projeto distribuído com **Docker**, **Python** e **OpenStack**, desenvolvido para realizar o envio, processamento e exibição de matrizes quadradas entre três máquinas virtuais distintas, utilizando comunicação via **sockets TCP/IP**.

## 🧩 Estrutura do sistema

O projeto é dividido em três programas independentes:

### 🔹 `p1` – Gerador de Matrizes
- Gera matrizes quadradas com números inteiros aleatórios.
- Envia as matrizes para o `p2` via socket TCP.
- Registra o tempo de envio.

### 🔹 `p2` – Processador
- Recebe as matrizes do `p1`.
- Inverte a matriz (se possível) e calcula seu determinante.
- Envia o resultado e o tempo para o `p3`.

### 🔹 `p3` – Exibidor
- Recebe os resultados do `p2`.
- Exibe o determinante da matriz e o tempo total desde a geração até a exibição.

Cada programa roda em uma VM diferente e em seu próprio container Docker.

---

## 📦 Imagens Docker (Docker Hub)

As imagens já estão publicadas e disponíveis no Docker Hub:

- [gxaierr/p1](https://hub.docker.com/r/gxaierr/p1)
- [gxaierr/p2](https://hub.docker.com/r/gxaierr/p2)
- [gxaierr/p3](https://hub.docker.com/r/gxaierr/p3)

Você pode executá-las diretamente em qualquer máquina com Docker instalado:

```bash
docker run -it gxaierr/p3   # Inicie o receptor final
docker run -it gxaierr/p2   # Inicie o processador intermediário
docker run -it gxaierr/p1   # Por último, o gerador de matrizes
