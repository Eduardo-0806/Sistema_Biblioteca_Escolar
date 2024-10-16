from controle.controle_emprestimos import ControleEmprestimos
from entidades.emprestimos import Emprestimos
from utilitarios.menus import limpar_console
from utilitarios.splash_screen import SplashScreen
from relatorio.relatorio import Relatorio 
from conexao_bd.mySQL_queries import MySQLQueries
import mysql.connector
import re
from datetime import date
from datetime import timedelta

dia = date.today() + timedelta(days=14)
print(dia)