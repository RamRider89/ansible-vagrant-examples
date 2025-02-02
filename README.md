# ansible-vagrant-examples
Ejemplos de vagrant con ansible

# pwd
./ansimble-vagrant-samples

# ANSIBLE
## GENERAR COLLECTION
ansible-galaxy collection init samples.wordpress

## GENERAR ROLES
cd samples/wordpress
ansible-galaxy role init roles/webserver
ansible-galaxy role init roles/dataserver


- ubicarse en el tipo de proyecto deseado
- editar los valores necesarios

# RUN
vagrant up

# STOP
vagrant halt

# DESTROY
vagrant destroy -f

# CHECK ANSIBLE
vagrant halt

# CHECK VIRTUALBOX
vboxmanage list runningvms
vboxmanage list vms