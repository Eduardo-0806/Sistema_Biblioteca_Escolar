# SISTEMA DE BIBLIOTECA ESCOLAR EM PYTHON
O sistema presente nesse repositório representa um sistema de emprestimo de livros utilizado por uma biblioteca escolar, composto por um conjunto de tabelas que para representar os emprestimos, sendo elas: __Livros, Alunos e Emprestimos__

## PREPARANDO PARA UTILIZAÇÃO DO SISTEMA

O sistema produzido exige que as tabelas já existam, portanto antes de rodar o programa principal, é necessário a execução do seguinte script em Python:

``` shell
~$ python criar_tabelas_registros.py
```

## INICIANDO O SISTEMA 

Tendo executado o script anteriormente mencionado e finalizado a criação das tabelas, junto com os registros de exemplo, basta executar o script principal do sistema:

``` shell
~$ python principal.py
```

## ORGANIZAÇÃO REPOSITÓRIO

- [Diagrama](Diagrama): Nesse diretório está contido o [diagrama relacional](Diagrama/DIAGRAMA_RELACIONAL_SISTEMA_BIBLIOTECA_ESCOLAR.pdf) do sistema, com suas entidades e relacionamentos.
  * As entidades representadas no diagrama são: ALUNOS, EMPRESTIMOS E LIVROS
- [sql_tabelas](sql_tabelas): Nesse diretório estão contidos os scripts SQL responsáveis pela criação das tabelas do sistema e da inserção de registros fictícios nessas tabelas.
  * [criar_tabelas_biblioteca_escolar.sql](criar_tabelas_biblioteca_escola.sql): Script SQL responsável pela criação das tabelas utilizadas no sistema, tal como os seus relacionamentos;
  *  [inserir_dados_tabelas_biblioteca_escolar.sql](inserir_dados_tabelas_biblioteca_escolar.sql): Script SQL responsável por inserir registros de exemplos nas tabelas do sistemas.
- [src](src): Nesse diretório estão guardados os scripts responsáveis pelo funcionamento do sistema
  * [conexao_bd](src/conexao_bd) - Nesse diretório está guardada a classe responsável por realizar a conexão do sistema com o banco de dados mySQL, tal como um arquivo responsável por guardar dados úteis para autentificação do usuário
    - [mySQL_queries.py](src/conexao_bd/mySQL_queries.py) - Classe responsável por realizar a conexão com o banco de dados, também realizando os comandos DML(como inserção, alteração ou exclusão de registros) e DDL(como a criação, alteração ou exclusão de tabelas), além das querys para os relatórios.
       + Exemplo da sua utilização para uma consulta simples:
         ``` python
         def listar_alunos(self):
         """
         Método listar_alunos - Responsável por realizar a listagem dos alunos cadastrados na tabela 'Alunos'
         Retorno: Retorna um DataFrame da biblioteca pandas contendo os alunos cadastrados
         """
         #Realiza conexão com o banco de dados
         conexao_listagem: MySQLQueries = MySQLQueries()
         conexao_listagem.connect()

         #Armazena em uma variável o código SQL para listar os alunos cadastrados
         query_verificacao = ("select matricula as 'Matricula do Aluno', nome as 'Nome Aluno', email as 'Email Aluno'" + "from ALUNOS order by nome;")
        
         #Retorna um DataFrame contendo a listagem dos alunos cadastrados
         return conexao_listagem.execute_query_dataframe(query_verificacao)
         ```
    - [autenticador_mySQL.](src/conexao_bd/autenticador/autenticador_mySQL.txt) - Arquivo contendo informações para conexão com o banco de dados, sendo respectivamente o nome do banco de dados, o usuário do banco de dados e a senha do banco de dados.
 * [controle](src/controle): Diretório onde estão contidas as classes responsáveis por controlar as operações de inserção, alteração e exclusão de cada tabela.
 * [entidades](src/entidades): Direstório onde estão contidas as classes que representam as entidades descritas no [diagrama relacional](Diagrama/DIAGRAMA_RELACIONAL_SISTEMA_BIBLIOTECA_ESCOLAR.pdf).
 * [relatorio](src/relatorio): Diretório onde está contida a classe responsável por controlar e realizar os relatórios do sistema.
 * [sql_relatorios](src/sql_relatorios): Diretório onde estão contidos os scripts SQL que geram as consultas exibidas nos relatórios.
 * [utilitarios](src/utilitarios): Diretórios onde estão contidas as classes responsáveis pela criação da Splash Screen e Menus exibidos ao decorrer do funcionamento do sistema.
 * [bibliotecas.txt](src/bibliotecas.txt): Arquivo de texto contendo as bibliotecas e suas respectivas versões utilizadas para o funcionamento do sistema.
 * [criar_tabelas_registros.py](src/criar_tabelas_registros.py): Script Python responsável pela criação das tabelas com seus relacionamentos, além de registros de exemplos.
 * [principal.py](src/principal.py): Script python responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados. Deve ser executado após a criação das tabelas.
