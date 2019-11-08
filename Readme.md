TODO:
	Alterar no aes.py o encrypt e decrypt para receberem a chave
	Usar as essas novas versões a partir da segunda mensagem por cada cliente
	


# Guião 6
Este guião segue a estrutura proposta pelo professor. O programa encontra-se separado em dois ficheiros, ***Server.py*** que responde aos pedidos dos clientes e o ficheiro ***Client.py*** que envia pedidos ao servidor.  

# Alterações Efetuadas

## Servidor
O servidor foi o ficheiro que sofreu o menor número de alterações. Ele simplesmente recebe e redireciona os pedidos recebidos. A segunda alteração é a indicação da terminação da execução de um cliente. Caso este envie uma mensagem vazia, o seu identificador é impresso e termina a conexão.  

## Cliente
 A alteração efetuada sobre o cliente fica mais facil de compreender coma observação do ficheiro ***aes.py***. Nesse ficheiro encontra-se uma implementação do algoritmo simetrico AES. O código desse algoritmo foi implementado sobre o cliente, antes do envio da mensagem ao servidor, o metudo `encrypt()` é invocado. Após a receção da resposta por parte do servidor, o metudo `decrypt()` é invocado. Assim o servidor apenas lida com **ciphertext**.
