# Nível 1 — PDV com Descontos

## O que o código faz

O `pdv.py` simula o caixa de uma loja. Para cada compra ele pede o valor e a idade do cliente, aplica os descontos de acordo com as regras (20% para clientes com 65 anos ou mais e mais 10% quando o valor, já com o desconto da idade, passa de R$ 100) e mostra o valor final em reais. Dá pra registrar quantas compras quiser; quando o valor digitado for `0` o caixa fecha e aparece o resumo do dia com a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como ele faz

1. Cria uma lista vazia `compras` para guardar o histórico.
2. Entra num `while True` e pede o valor da compra.
3. Se o valor for `0`, sai do loop com `break`.
4. Se o valor for negativo, mostra um aviso e volta pro início com `continue`.
5. Pede a idade. Se for negativa, mesmo esquema: aviso + `continue`.
6. Pede a quantidade de itens e o cupom (bônus — dá pra só apertar Enter nos dois).
7. Começa com `valor_final = valor` e aplica as regras **nessa ordem**:
   - idade `>= 65` → multiplica por `0.8` (20% off);
   - se o `valor_final` (já com o desconto da idade) for `> 100` → multiplica por `0.9` (10% off);
   - quantidade `> 3` → multiplica por `0.95` (5% off, bônus);
   - cupom `FIDELIDADE10` → multiplica por `0.9` (10% off, bônus).
   
   Depois de cada desconto o valor é arredondado com `round(..., 2)`.
8. Mostra quais descontos entraram e o valor final formatado (`R$ 144.00`).
9. Guarda a compra na lista com `compras.append(...)`.
10. Quando o loop termina, percorre a lista com um `for` somando o total bruto, os descontos e o total final, e mostra o resumo.
11. Grava o mesmo resumo (com cada compra) no arquivo `resumo.txt` (bônus).

## Como rodar

Precisa de Python 3 instalado. Dentro da pasta `nivel_1`:

```bash
python3 pdv.py
```

Exemplo de uso:

```
===== PDV - CAIXA =====
Digite 0 no valor para fechar o caixa

Valor da compra: R$ 200
Idade do cliente: 65
Quantidade de itens (enter = 1):
Cupom (enter se nao tiver):
Descontos: idade 20%, valor 10%
Valor final: R$ 144.00

Valor da compra: R$ 0

===== RESUMO DO DIA =====
Compras registradas: 1
Total bruto: R$ 200.00
Total de descontos: R$ 56.00
Total final: R$ 144.00

Resumo salvo em resumo.txt
```

## Tabela de exemplos (casos de teste)

Para conferir, digite o valor e a idade e deixe quantidade e cupom em branco (Enter).

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|-----------:|------:|:--------------:|:--------------:|---------------------:|
| 1 | 50.00 | 30 | 0% | 0% | **R$ 50.00** |
| 2 | 100.00 | 30 | 0% | 0% | **R$ 100.00** |
| 3 | 80.00 | 65 | 20% | 0% | **R$ 64.00** |
| 4 | 100.00 | 70 | 20% | 0% | **R$ 80.00** |
| 5 | 125.00 | 70 | 20% | 0% | **R$ 100.00** |
| 6 | 200.00 | 30 | 0% | 10% | **R$ 180.00** |
| 7 | 101.00 | 30 | 0% | 10% | **R$ 90.90** |
| 8 | 200.00 | 65 | 20% | 10% | **R$ 144.00** |
| 9 | 1000.00 | 80 | 20% | 10% | **R$ 720.00** |
| 10 | 200.00 | 64 | 0% | 10% | **R$ 180.00** |

Rodando os 10 em sequência, o resumo fica: 10 compras, total bruto **R$ 2156.00**, descontos **R$ 447.10**, total final **R$ 1708.90**.

### Casos que pegam

- **Caso 2** (`100`, 30): 100 não é *maior* que 100, então não tem os 10%.
- **Caso 5** (`125`, 70): `125 × 0.8 = 100`. Mesma coisa, fica em R$ 100.00.
- **Caso 7** (`101`, 30): `101 × 0.9 = 90.90` — por isso o arredondamento em duas casas.
- **Caso 10** (`200`, 64): 64 anos ainda não ganha o desconto de idade, só o de valor.

## Bônus implementados

| Bônus | Como usar |
|-------|-----------|
| Desconto por quantidade | Se digitar mais de 3 itens, entra 5% extra. Enter = 1 item. |
| Cupom de fidelidade | Digitar `FIDELIDADE10` (maiúscula ou minúscula) dá 10% extra. Outro cupom é ignorado com aviso. |
| Salvar histórico | Ao fechar o caixa é criado o `resumo.txt` na pasta onde o programa foi rodado. |

Os bônus são aplicados depois das duas regras principais, então não mudam nenhum dos 10 casos de teste.
