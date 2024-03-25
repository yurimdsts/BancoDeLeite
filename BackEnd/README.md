# BancoDeLeite
Projeto para auxiliar na coleta do Banco De Leite de Sorocaba

flask db init  # Inicia o repositório de migrations
flask db migrate  # Gera os arquivos de migration
flask db upgrade  # Aplica as migrations ao banco de dados

flask db init: Este comando é usado para inicializar um diretório de migrações na sua aplicação. Ele cria uma pasta migrations no seu projeto, onde os arquivos de migração serão armazenados. Você só precisa executar este comando uma vez para configurar o repositório de migrações.

flask db migrate: Quando você modifica seus modelos (por exemplo, adicionando uma nova classe de modelo ou alterando um campo existente), você usa este comando para gerar automaticamente um arquivo de migração no diretório migrations/versions. Esse arquivo contém as instruções necessárias para aplicar as mudanças ao banco de dados (como adicionar uma nova tabela ou coluna). O comando tenta detectar automaticamente as mudanças feitas nos modelos em relação ao esquema atual do banco de dados, mas é sempre uma boa prática revisar o arquivo de migração gerado para garantir que as alterações estão corretas.

flask db upgrade: Depois de revisar (e potencialmente ajustar) o arquivo de migração gerado pelo comando migrate, você usa upgrade para aplicar as mudanças ao banco de dados. Este comando atualiza o esquema do banco de dados para corresponder ao estado atual dos seus modelos, executando as instruções definidas no último arquivo de migração.

flask db downgrade: Se você precisar desfazer a última migração aplicada, pode usar este comando para reverter as mudanças. Isso é útil em casos onde a migração mais recente causou um problema ou não era o que você pretendia.