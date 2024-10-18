__README temporário__
<p>Readme será, por enquanto, unicamente para propósito de informar bibliotecas e o necessário para utilização do projeto nas maquinas virtuais de cada componente
Logo, isso será mudado até a última versão do projeto</p>

# Passos Necessários Para Execução do Projeto

## Bibliotecas necessárias
<p>Primeiro de tudo, vocês precisam baixar as bibliotecas para que a conexão com o banco de dados mySQL e a exibição dos relatórios sejam feitas.</p>
<p>Para isso baixem todos os arquivos e pastas do projeto, entre eles, dentro do diretório 'src', terá um arquivo chamado 'bibliotecas.txt'.
Através do prompt de comando, utilizando os comandos:</p>
<p><code>dir</code>(Para Exibir os diretórios que você pode caminhar) e <code>cd >Nome Diretório<</code>(Vai para o diretório passado após o cd)</p>
<p>Vocês devem caminhar pelos diretórios do computador, até vocês encontrarem a pasta/diretório onde estão salvas as pastas do projeto</p> 
<p>Nisso, vocês realizam mais um cd para entrar no diretório src após isso, basta digitar no prompt de comando o seguinte código:</p>
<p> <code>pip install -r bibliotecas.txt </code></p>
<p>Se tiverem caminhado corretamente até o diretório, o prompt de comando(Vulgo terminal) vai mostrar o progresso do download das bibliotecas</p>
<p>Tendo finalizado essa parte, deve ser realizado o próximo passo</p>

## Criando Tabelas
<p>Se vocês baixaram corretamente as bibliotecas, antes de executar o programa principal, vocês devem executar o script para criação de tabelas e seus registros</p>
<p>Sem as tabelas, o funcionamento do programa será travado</p>
<p>Portanto, realizem o mesmo caminho para chegar ao diretório src, onde encontraram o arquivo "biblioteca.txt" e realizem o seguinte comando:</p>
<p><code>python criar_tabelas_registros.py</code></p>
<p>Uma sequência de comandos será exibida no terminal, se no final delas estiver escrito <b>"Registros inseridos com sucesso"</b>, significa que o processo deu certo</p>

## Executando O Programa
<p>Por fim, tendo executado os passos anteriores corretamente, basta, estando no mesmo diretório/pasta dos outros 2 arquivos, executar o seguinte comando:</p>
<p><code>python principal.py</code></p>
<p>Se tudo acontecer corretamente, o programa irá exibir a tela splash(Com nome dos Componentes do grupo) e executar o restante do sistema</p>

## Objetivo
<p>Simplesmente testem, tentem de todas as formas fazer o programa dar <b>erro, travar ou qualquer coisa de gravidade semelhante</b>, se isso acontecer ou outro erro do tipo
printem e mandem no grupo para eu poder corrigir(Ou corrijam vocês mesmo se sentirem tranquilos para tal), se notarem algum erro de lógica ou algum aspecto que possam melhorar,
façam a mesma coisa e mandem no grupo</p>
<p>Se lembrem, os testes devem ser feitos na <b>MÁQUINA VIRTUAL</b>, disponibilizada no Ava, para sabermos que está tudo certo</p>
