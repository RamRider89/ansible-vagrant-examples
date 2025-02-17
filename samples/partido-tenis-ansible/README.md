# Materia: Herramientas de Automatización de Despliegues
# Actividad: Desarrollo práctico
# Alumno: Carlos David Duarte Gill
# Grupo: 1030
# Fecha 17 de febrero de 2025

# Contenido del proyecto

partido-tenis-ansible/
├── Vagrantfile
├── ansible/
│   ├── hosts
│   ├── roles/
│   │   └── generar_partido/
│   │       ├── tasks/
│   │       │   └── main.yml
│   │       ├── vars/
│   │       │   ├── main.yml
│   │       │   └── partido_vars.yml
│   │       │ 
│   │       └── templates/
│   │           └── partido.txt.j2
│   └── playbook.yml
└── partido_vars.yml

## Proceso
- Se genero el proyecto dentro de la carpta partido-tenis-ansible
➜  cd partido-tenis-ansible
- Se inicializo vagrant
➜  vagrant init
- Se genero el rol mediante galaxy
➜  ansible-galaxy init generar_partido      

## Ejecución
- para levantar la maquina
➜  vagrant up
- para ejecutar ansible
➜  vagrant provision
- para acceder a la maquina
➜  vagrant ssh
- para comprobar que se genero el archivo
➜  cat /vagrant/partido.txt

## Nota
En caso de ocurrir un error durante la creacion de la maquina virtual, en la fase Installing Ansible...
Solo ejecutar el comando:
➜  vagrant provision