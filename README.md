# SEL0337
Prática 5 - Projetos em Sistemas Embarcados

Alunos: Eduardo José Carvalho (12695307); Filipe Cerqueira (8657605)

OBJETIVO: 
1: Inicializar automaticamente um programa quando a placa Raspberry Pi inicializar o sistema operacional.
2: Conhecer/utilizar o Github como repositório.

Funcionamento:
Ao dar boot o sistema carrega e inicializa o programa blink.py que tem como função fazer um led vermelho piscar mostrando que o programa está ativo. Caso a execução do programa blink.py pare, entra o programa blink_stop.py que acente um led verde para mostrar que blink.py não está mais ativo e que é necessário um novo boot no sistema.

O grupo utilizou de 3 programas: 
1: blink.py = faz piscar um led vermelho na inicialização do sistema operacional.
2: blink_stop.py = faz um led verde acender caso o programa blink.py pare de funcionar
3: blink.service = onde colocamos a especificação do serviço que vai ser inicializado. 
