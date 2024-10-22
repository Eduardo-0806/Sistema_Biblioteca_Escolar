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
    - [autenticador_mySQL.](src/conexao_bd/autenticador/autenticador_mySQL.txt) - Arquivo contendo informações para conexão com o banco de dados, sendo respectivamente o nome do banco de dados, o usuário do banco de dados e a senha do banco de dados.

