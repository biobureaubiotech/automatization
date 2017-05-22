"""Codigo em Python que pára (stop) automaticamente uma instancia 
   logo após finalizar um comando. O input requerido é o comando
   a ser executado. """

import subprocess

comando = input("Cole aqui o comando a ser executado:")   #Solicita o comando a ser rodado
subprocess.call(comando, shell=True)   #Roda o comando
pipe = subprocess.Popen("wget -q -O - http://169.254.169.254/latest/meta-data/instance-id",
                        shell=True, stdout=subprocess.PIPE).stdout   #Obtem o ID da instância atual
output = pipe.read().decode("utf-8")   #Transforma byte (pipe) em string (output), com decodificacao utf-8
subprocess.call("aws ec2 stop-instances --instance-ids " + output, shell=True)   #Pára a instância atual
