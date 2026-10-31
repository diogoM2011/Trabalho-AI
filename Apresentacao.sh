#!/bin/bash

MAIN_WINDOW_ID=$(xdotool getactivewindow)

for i in {1..5}
do
    if (( i == 1 )) then
        gnome-terminal -- bash -c "printf '\e[8;30;90t' ; slides Apresentação1.md ; echo; read -p 'Command Concluded, press Enter to close the terminal...'" &
        sleep 0.2
        xdotool windowactivate "$MAIN_WINDOW_ID"
        read -p "Pressione Enter para abrir o proximo slide"
    elif (( i == 2 )) then 
        gnome-terminal -- bash -c "printf '\e[8;30;90t' ; slides Apresentação2.md ; echo; read -p 'Command Concluded, press Enter to close the terminal...'" &
        sleep 0.2
        xdotool windowactivate "$MAIN_WINDOW_ID"
        read -p "Pressione Enter para abrir o proximo slide"
    elif (( i == 3 )) then
        gnome-terminal -- bash -c "printf '\e[8;30;90t' ; slides Apresentação3.md ; echo; read -p 'Command Concluded, press Enter to close the terminal...'" &
        sleep 0.2
        xdotool windowactivate "$MAIN_WINDOW_ID"
        read -p "Pressione Enter para abrir o proximo slide"
    elif (( i == 4 )) then
        gnome-terminal -- bash -c "printf '\e[8;30;90t' ; slides Apresentação4.md ; echo; read -p 'Command Concluded, press Enter to close the terminal...'" &
        sleep 0.2
        xdotool windowactivate "$MAIN_WINDOW_ID"
        read -p "Pressione Enter para abrir o proximo slide"
    elif (( i == 5 )) then
        gnome-terminal -- bash -c "printf '\e[8;30;90t' ; slides Apresentação5.md ; echo; read -p 'Command Concluded, press Enter to close the terminal...'" &
        sleep 0.2
        xdotool windowactivate "$MAIN_WINDOW_ID"
        read -p "Pressione Enter para fechar a apresentação"
    fi
done