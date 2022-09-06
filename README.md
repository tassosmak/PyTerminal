# PyTerminal

PyTerminal is a somewhat terminal interface that still bases on the terminal of your computer(Unix/Windows)

It has 2 Modes:

### The Basic Mode 
it limits the function to the absoloute basic 

### The Advanced Mode 
that offers a bit more features than the basic 

i have also a added a 999 mode but it doesn't serve any purpose it's just for testing purposes :)

## How it Works:
essentially its just an input that then calls a function that procces the input and deliever an 
output based on the mode you are and the parameters that have been set

## Full Details on Commit No.85:
1) every time you launch the program history.log adds the date and hour of the current sension it runs
2) added platform identifier to optimixe the sys commands to improve reliability(for the time it only support the already only supported platforms although it should work to every linux distro to NOT SURE YET)
3) changed from mode 999 to mode 9 to avoid bugs
4) deleted class WorkSpaceHandler to minimize bugs
5) deleted some comments
6) improved the check of multiple instanches at the same time from now it will just not respond to commands that require internet
# 0.3 Alpha coming soon
