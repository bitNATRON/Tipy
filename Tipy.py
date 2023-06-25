import os
import platform
import subprocess
import random
import shutil

operating_system = platform.system()
print(f"Olá! Que tal aprender esse novo comando de {operating_system}:\n")

if operating_system == "Windows":
  cmdlet_list_command = 'powershell.exe Get-Command -CommandType Cmdlet | Select-Object -ExpandProperty Name'
  output = subprocess.run(cmdlet_list_command, capture_output=True, text=True)
  cmdlets = output.stdout.splitlines()
  random_cmdlet = random.choice(cmdlets)
  help_param = "Get-Help"
else:
  path_dirs = os.environ["PATH"].split(":")
  shell_commands = ["bash", "sh"]
  help_param = "--help"

  all_commands = []
  if operating_system != "Windows":
    for dir in path_dirs:
      commands = os.listdir(dir)
      for cmd in commands:
        full_cmd_path = os.path.join(dir, cmd)
        if os.access(full_cmd_path, os.X_OK) and shutil.which(cmd):
          all_commands.append(full_cmd_path)

    random_command = random.choice(all_commands)

    if operating_system != "Windows" and random_command:
      apropos_output = subprocess.run(['apropos', '-s', '1', '.'], capture_output=True, text=True)
      commands = apropos_output.stdout.splitlines()
      random_command = random.choice(commands).split(' ')[0]

if operating_system == "Windows":
  subprocess.run(['powershell.exe', help_param, random_cmdlet])
else:
  if stdout:
    print(stdout.decode())
  if stderr:
    print(stderr.decode())