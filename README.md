# Battle Simulator Project

This was a little project I wrote after completion of my first Python course to try to exercise some of my skills that I learned. It allows a user to create monsters and pit them against each other in a battle reminiscent of Pokemon, allowing the user to continue battling with the winner. 

### Files:
#####Attacks.py:
This file contains an Attacks class, providing the framework to create new attack objects easily. All existing attacks are listed at the bottom of the file.
#####Monsters.py:
This file contains a dictionary of all predefined monsters using an identifier as a key and a tuple with the species name, max health, and 2 attacks imported from Attacks.py. It then provides the framework to create new monster objects to add to said dictionary with the Monster class, as well as various methods for information display and what to do in a battle or upon battle end.
#####Battle.py:
This is the executable file. Defines functions for selecting a monster and for battling with selected monsters. The code that is executed allows the user to select the 2 monsters they wish to have battle against one another, have them battle, and select another monster to fight with the winner if they so please. At the end is a list of bugs and features to be implemented for myself to reference back to for future updates, also copied below:

------------------------CURRENT BUGS-----------------------------------------------------------------
* Status effects only applying their effects for one turn

------------------------TO BE IMPLEMENTED -----------------------------------------------------------
* implement super effective and not very effective attacks
* allow for saving of a monster to a csv file that can be loaded up later
* allow for saving of attacks to a csv file that can be referenced later

-----------------------------------------------------------------------------------------------------
