This project has been made by Ishac Bertran, and aims to introduce children to animation through the stop motion technique.



Link to the original project : http://pasapas-project.com/

Link to Ishac's website : http://www.ishback.com/

For this particular realization, the contributors are:

Association Electroni[K] - Florine Rupin;

Design and building - Corentin Le Bris;

Software developpement - Rodolphe Dugueperoux, Adrien Schmouker.


~~~
Electronic diagram
~~~
![Electronic diagram](https://github.com/duguep/Pas-a-pas/blob/master/Electronic.png)
~
Button Record: 		GPIO 4

Button Previous:   	GPIO 17

Button Next:		GPIO 18

Button Delete:		GPIO 27

Button Play:		GPIO 22

Button Stop:		GPIO 23

Button Save:   		GPIO 24

Switch cercle:   	GPIO 13
switch triangle: 	GPIO 6
switch playback: 	GPIO 19

Switch 3 entries:

Assistant mode:    	GPIO 26

Free mode:	       	GPIO 20

~~~
Install
~~~

~
Pas-a-Pas Installation (code)
~

Install a graphic debian in the rapsberry pi.
When the raspberry pi is ready, open terminal and make this command.
~~~
      sudo apt-get install libopencv-dev python-opencv -> installation of opencv
      sudo apt-get install libgl1-mesa-dri
      sudo apt-get install unclutter -> To take of the mouse icon
      sudo apt-get install x11-xserver-utils -> To take of standby
~~~

For autostart Pas-a-Pas program.
sudo nano /etc/xdg/lxsession/LXDE/autostart
Add this lines.
~~~
	@xset s off
	@xset -dpms
	@xset s noblank
	@lxterminal
~~~

Edit .bashrc on /home/pi 
and add
~~~
sleep 5
#chemin du dossier pas-a-pas
cd ./Pas_a_pas
unclutter -idle 0.1 & sudo python main.py
~~~

Edit autostart.

sudo nano ~/.config/lxsession/LXDE/autostart

Ajoutez la ligne
~~~
	@lxterminal
~~~

Check if the GPIO is Opened.
http://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/#LII-D-3