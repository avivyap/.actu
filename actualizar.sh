#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

trap ctrl_c INT
function ctrl_c(){
        echo -e "\n${redColour}[+] Saliendo........${endColour}\n"
        tput cnorm; exit 1
}


function no_actu(){

        echo -e "\n${purpleColour}[+]${endColour}${yellowColour} Hay varios paquetes que no se pueden actualizar, asi que tienes que hacerlo a mano${endColour}\n"
        apt list --upgradable 2>/dev/null
        echo -e "\n${purpleColour}[+]${endColour}${yellowColour} [+] Para actualizarlos es --->${endColour}${blueColour}   sudo apt upgrade x ${endColour}${yellowColour}<- x es el nombre del paquete${endColour}\n"
        tput cnorm; exit 0
}

function actualizar(){

        echo -e "\n${purpleColour}[+]${endColour}${yellowColour} Se han encontrado paquetes sin actualizar${endColour}\n"
        sudo apt upgrade -y > /dev/null 2>&1
        comprobacion

}
function todo_actu(){

        echo -e "\n${purpleColour}[+]${endColour}${greenColour} Todo esta actualizado${endColor}\n"
        tput cnorm; exit 0
}

function comprobacion(){
        ((trys++))
        if [ $trys == 3 ];then

                no_actu

        else
                if [ "$(sudo apt update 2>/dev/null | tail -n 1)" == "Todos los paquetes están actualizados." ];then
                        todo_actu
                else
                        actualizar
                fi
        fi
}



#main
declare -i trys=0
tput civis;clear
if [ $(id -u) == "0" ];then

        comprobacion

else
        echo -e "\n${purpleColour}[+]${endColour}${redColour} No estas ejecutando el script como root${endColour}\n"
        tput cnorm; exit 1
fi
