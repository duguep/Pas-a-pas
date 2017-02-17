This project has been made by Ishac Bertran, and aims to introduce children to animation through the stop motion technique.



Link to the original project : http://pasapas-project.com/

Link to Ishac's website : http://www.ishback.com/

For this particular realization, the contributors are:

Association Electroni[K] - Florine Rupin;

Design and building - Corentin Le Bris;

Software developpement - Rodolphe Dugueperoux, Adrien Schmouker.


~~~
Schema electronique
~~~

record GPIO 4

prev   GPIO 17

next   GPIO 18

delete GPIO 27

play   GPIO 22

stop   GPIO 23

save   GPIO 24

switch cercle   GPIO 13
switch triangle GPIO 6
switch playback GPIO 19

Switch 3 entrées

mode assisté    GPIO 26

mode free       GPIO 20

~~~
Installation
~~~

~
Installation electronique voir Schema.
~

~
Installation Pas-à-Pas (code)
~


Installez Debian graphique sur la rapsi

Faire ces commandes bash.
~~~
      sudo apt-get install libopencv-dev python-opencv -> installation d'opencv
      sudo apt-get install libgl1-mesa-dri
      sudo apt-get install unclutter -> enlever l'affichage de la souris
      sudo apt-get install x11-xserver-utils -> enlever la mise en veille
~~~

Pour autodémarrez le programme -> 
sudo nano /etc/xdg/lxsession/LXDE/autostart
Ajoutez ces lignes
~~~
	@xset s off
	@xset -dpms
	@xset s noblank
	@lxterminal
~~~

Modifiez le .bashrc dans le /home/pi 
et ajoutez

~~~
sleep 5
#chemin du dossier pas-à-pas
cd ./Pas_a_pas
unclutter -idle 0.1 & sudo python main.py
~~~

Modifiez l'autostart

sudo nano ~/.config/lxsession/LXDE/autostart

Ajoutez la ligne
~~~
	@lxterminal
~~~