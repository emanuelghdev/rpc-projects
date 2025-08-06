#!/bin/sh -e
# ejecutar = Macro para compilación y ejecución del programa ejemplo
# en una sola maquina Unix de nombre localhost.

echo
echo "Lanzando el ligador de RMI ... "
rmiregistry &

echo
echo "Compilando con javac ..."
javac *.java

sleep 2

echo
echo "Lanzando el primer servidor"
java -cp . -Djava.rmi.server.codebase=file:./ -Djava.rmi.server.hostname=localhost -Djava.security.policy=server.policy Servidor1 &

sleep 2

echo
echo "Lanzando el segundo servidor"
java -cp . -Djava.rmi.server.codebase=file:./ -Djava.rmi.server.hostname=localhost -Djava.security.policy=server.policy Servidor2 &

sleep 2

echo
echo "Lanzando el cliente"
echo
java -cp . -Djava.security.policy=server.policy Cliente
