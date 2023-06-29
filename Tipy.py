import os
import subprocess
import random

class ExploradorComandos:
    def __init__(self):
        self.sistema_operacional = os.name

    def exibir_inicio(self):
        inicios_windows = [
            "Aopa! Que tal aprender um novo comando do Windows hoje?",
            "Bem-vindo ao mundo dos cmdlets! Vamos explorar juntos!",
            "Prepare-se para descobrir o poder dos comandos do Windows e suas (finitas...) possibilidades.",
            "Saudações, explorador do prompt de comando! Aprenda e ganhe uma melhor prompt-ção na vida!",
            "Esteja preparado para liberar todo o poder dos comandos do Windows! Sua jornada no prompt de comando começa!"
        ]

        inicios_unix = [
            "Bem-vindo, lorde das núvens baseadas em {} dos reinos compatíveis com o POSIX...".format(self.sistema_operacional),
            "Adentre o reino Linux de GNU, e libere sua habilidade no prompt de comando!",
            "Abraçe a magia do UNIX e torne-se o maestro da sua sinfonia no terminal!",
            "Saudações, usuário criativo de UNIX! Suas habilidades no prompt de comando são uma verdadeira obra de arte!",
            "Aprender sobre UNIX é saudavel! Com ele vem bastante 'Vi-tamina C++', então vá em frente!"
        ]

        if self.sistema_operacional == "nt":
            inicios = inicios_windows
        else:
            inicios = inicios_unix

        inicio = random.choice(inicios)
        print(f"{inicio}\n")

    def obter_comandos_windows(self):
        comando_listar_cmdlets = 'powershell.exe Get-Command -CommandType Cmdlet | Select-Object -ExpandProperty Name'
        listagem = subprocess.run(comando_listar_cmdlets, capture_output=True, text=True)
        cmdlets = listagem.stdout.splitlines()
        return cmdlets

    def obter_comandos_unix(self):
        path_dirs = os.environ["PATH"].split(":")
        comandos_executaveis = []
        for directory in path_dirs:
            if os.path.isdir(directory):  # Importante: Verificação
                for cmd in os.listdir(directory):
                    caminho_completo_cmd = os.path.join(directory, cmd)
                    if os.access(caminho_completo_cmd, os.X_OK):
                        comandos_executaveis.append(caminho_completo_cmd)
        return comandos_executaveis

    def executar_comando_aleatorio(self):
        if self.sistema_operacional == "nt":
            parametro_help = "Get-Help"
            cmdlets = self.obter_comandos_windows()
            cmdlet_aleatorio = random.choice(cmdlets)

            subprocess.run(['powershell.exe', parametro_help, cmdlet_aleatorio])
        else:
            parametro_help = "--help"
            comandos_executaveis = self.obter_comandos_unix()
            comando_aleatorio = random.choice(comandos_executaveis)
            print(f"NOME:{comando_aleatorio}\n")

            subprocess.run([comando_aleatorio, parametro_help])

explorador = ExploradorComandos()
explorador.exibir_inicio()
explorador.executar_comando_aleatorio()
