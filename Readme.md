# Calculadora distribuida python
Aluno: Gustavo Mota Barros
Matricula: 202104971

## Biblioteca Utilizada
 - Pyro5

## Funcoes
 - soma(a, b) retorna a + b
 - subtrai(a, b) retorna a - b
 - multiplica(a, b) retorna a * b
 - divide(a, b) retorna a / b
 - raiz(a) retorna a**(1/2)
 - potencia(a, b) retorna a**b 

 ## Comandos necessarios para subir a calculadora

 O primeiro passo consiste em executar o modulo responsavel por subir o nameserver escutando em todas as interfaces
 ```
 python3 -m Pyro5.nameserver -n 0.0.0.0
 ```

 Depois deve-se executar o codigo que implementa e sobe a calculadora
 ```
python3 remote_calc.py
 ```

 E agora o cliente
 ```
 python3 client.py
 ```

 Com isso podemos acessar os metodos dos objetos remotos de outras maquinas, conectadas na mesma rede.
