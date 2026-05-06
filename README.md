# Custom Exceptions (Python)

This project demonstrates how to build and use custom exceptions in Python using two approaches:

- Regular classes
- Dataclasses

---

## 🇺🇸 English

### Overview

The project contains:

- A base exception: `Error`
- A specific business exception: `InsufficientBalanceError`
- Dataclass-based equivalents:
  - `ErrorDataclass`
  - `InsufficientBalanceErrorDataclass`

Main goal: show how to centralize exception messages for logs and client-facing output.

### Project Structure

```text
core/
  exceptions/
    __init__.py
    exceptions.py
    exceptions_with_dataclass.py
main.py
main_dataclass.py
```

### Requirements

- Python 3.10+

### How to Run

Run regular exception example:

```bash
python main.py
```

Run dataclass exception example:

```bash
python main_dataclass.py
```

On Windows, if `python` is not available:

```bash
py -3 main.py
py -3 main_dataclass.py
```

### What You Will See

- How exceptions are raised and caught
- `__str__` and `__repr__` behavior
- Separate messages for:
  - Logs (`msg_log`)
  - Client/UI (`msg_cliente`)

### Notes

- This repository is focused on learning and structure.
- You can rename fields like `msg_log` and `msg_cliente` to fully English naming if desired.

---

## 🇧🇷 Português

### Visão Geral

Este projeto demonstra como criar e usar exceções customizadas em Python com duas abordagens:

- Classes tradicionais
- Dataclasses

O projeto contém:

- Uma exceção base: `Error`
- Uma exceção de negócio: `InsufficientBalanceError`
- Versões equivalentes com dataclass:
  - `ErrorDataclass`
  - `InsufficientBalanceErrorDataclass`

Objetivo principal: centralizar mensagens de exceção para logs e para saída ao cliente.

### Estrutura do Projeto

```text
core/
  exceptions/
    __init__.py
    exceptions.py
    exceptions_with_dataclass.py
main.py
main_dataclass.py
```

### Requisitos

- Python 3.10+

### Como Executar

Executar exemplo com exceções tradicionais:

```bash
python main.py
```

Executar exemplo com dataclass:

```bash
python main_dataclass.py
```

No Windows, se `python` não estiver disponível:

```bash
py -3 main.py
py -3 main_dataclass.py
```

### O Que Você Vai Ver

- Como as exceções são lançadas e tratadas
- Comportamento de `__str__` e `__repr__`
- Mensagens separadas para:
  - Log (`msg_log`)
  - Cliente/UI (`msg_cliente`)

### Observações

- Este repositório é focado em aprendizado e organização.
- Se quiser, você pode renomear `msg_log` e `msg_cliente` para nomes 100% em inglês.

