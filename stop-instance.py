"""Codigo em Python que pára automaticamente uma instancia logo após
   finalizar um comando."""

import subprocess

#Requer o comando a ser rodado
comando = input("Cole aqui o comando a ser executado:")
#Roda o comando
subprocess.call(comando, shell=True)
#Obtem o ID da instância atual
pipe = subprocess.Popen("wget -q -O - http://169.254.169.254/latest/meta-data/instance-id",
                        shell=True, stdout=subprocess.PIPE).stdout
output = pipe.read().decode("utf-8")
#Pára a instância atual
subprocess.call("aws ec2 stop-instances --instance-ids " + output, shell=True)
