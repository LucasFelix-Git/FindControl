# Modelo Relacional
![Modelo Relacional](/img/MRv1.png)
## Entidades

- Usuário
- Receita
- Despesa
- Categoria

## Relacionamentos

- Um usuário possui várias receitas.
- Um usuário possui várias despesas.
- Uma categoria pode estar associada a várias receitas.
- Uma categoria pode estar associada a várias despesas.

## Regras

- O saldo não é armazenado, ele é calculado.
- Toda receita pertence a um usuário e a uma categoria.
- Toda despesa pertence a um usuário e a uma categoria.