#%%
import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
mc.postToChat("Hot baby peanutbutter!")



#%%

3 * 3

#%%
"W" + "o" * 999

#%%

print(2 + 2)
print("W" + "o" * 20)
print("PYTHON!")
print("<3s")
print("Minecraft")

bread = 999

pickaxes = 12, iron = 30, cobblestone = 25

#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

x = -479
y = 821
z = 178

mc.player.setTilePos(x, y, z)

#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

x = -192.0
y = 93.0
z = -240.0

mc.player.setPos(x, y, z)
#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

x = 0.0
y = - 5.0
z = 0.0

mc.player.setPos(x, y, z)

#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

x = -1.333
y = -20.0
z = -20.135

mc.player.setPos(x, y, z)
#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

#x = -266 - -192 = -266 + 192 = -74
#y(height) = 63.0 - 93 = - (63+93)  
#z = -233.5 - -240 = 6.5

mc.player.setPos(x, y, z)

#%%


#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

target_x = -266
target_y = 63
target_z = -233.5
spawn_x = -192
spawn_y = 93
spawn_z = -240

x = target_x - spawn_x
y = target_y - spawn_y
z = target_z - spawn_z

mc.player.setPos(x, y, z)

#%%
x, y, z

#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

def teleport(target_x, target_y, target_z, spawn_x, spawn_y, spawn_z):
    """Teleport a random player to the target position relative to the spawn position.
    
    
        Args:
            target_x, ...: target position where the player will be teleported
            spawn_x, ...: absolute psoition of the spawn point.
        """

    x = target_x - spawn_x
    y = target_y - spawn_y
    z = target_z - spawn_z

    mc.player.setPos(x, y, z)

target_x = -150
target_y = 76
target_z = -188
spawn_x = -192
spawn_y = 93
spawn_z = -240

teleport(-266, 63, -233, -192, 93, -240)

time.sleep(10)

 #%%
x, y, z

#%%
from mcpi.minecraft import Minecraft 
mc = Minecraft.create("smalldell1")

def teleport(target_x, target_y, target_z, spawn_x, spawn_y, spawn_z):
    """Teleport a random player to the target position relative to the spawn position.
    
    
        Args:
            target_x, ...: target position where the player will be teleported
            spawn_x, ...: absolute psoition of the spawn point.
        """

target_x = -266
target_y = 63
target_z = -233.5
spawn_x = -192
spawn_y = 93
spawn_z = -240

x = target_x - spawn_x
y = target_y - spawn_y
z = target_z - spawn_z

teleport(-266, 63, -233.5, -192, 93, -240)

time.sleep(4)

mc.player.setPos(x, y, z)

time.sleep(4)

target_x = -132.4
target_y = 83
target_z = -167.8
spawn_x = -192
spawn_y = 93
spawn_z = -240

x = target_x - spawn_x
y = target_y - spawn_y
z = target_z - spawn_z

teleport(-132, 83, -167, -192, 93, -240)

time.sleep(4)


target_x = -102.374
target_y = 74
target_z = 439.5
spawn_x = -192
spawn_y = 93
spawn_z = -240

x = target_x - spawn_x
y = target_y - spawn_y
z = target_z - spawn_z

teleport(11, 63, -502, -192,  93, -240)


mc.player.setPos(x, y, z)

#%%
x = target_x - spawn_x
y = target_y - spawn_y
z = target_z - spawn_z

target_x = -102.374
target_y = 74
target_z = 439.5
spawn_x = -192
spawn_y = 93
spawn_z = -240

teleport(11, 63, -502, -192,  93, -240)

#%%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

x = 0
y = 2
z = 0
blockType = 45
mc.player.setPos(x, y, z, blockType)
||#%%


#%%
print(3 + 3, 2 + 1)



#%%
x = 0
y = 3
z = 0
blockType = 57
mc.setBlock(x, y, z, blockType)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

y = y + 1
mc.setBlock(x, y, z, 57)

#%%
from mcpi.minecraft import Minecraft

#%%
pos = mc.player.getTilePos()
x = pos.x 
y = pos.y + 2
z = pos.z
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y + 1
z = pos.z
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x - 1
y = pos.y + 1
z = pos.z
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x 
y = pos.y + 1
z = pos.z - 1
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x 
y = pos.y + 1
z = pos.z + 1
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y 
z = pos.z
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x - 1
y = pos.y 
z = pos.z
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x 
y = pos.y 
z = pos.z - 1
blockType = 103
mc.setBlock(x, y, z, blockType)

pos = mc.player.getTilePos()
x = pos.x 
y = pos.y 
z = pos.z + 1
blockType = 103
mc.setBlock(x, y, z, blockType)

#%%
pos = mc.player.getTilePos()
x = pos.x 
y = pos.y 
z = pos.z
blockType = 101
mc.setBlock(x, y + 3, z, blockType)
mc.setBlock(x + 1, y + 1, z, blockType)
mc.setBlock(x - 1, y + 1, z, blockType)
mc.setBlock(x , y + 1, z - 1, blockType)
mc.setBlock(x , y + 1, z + 1, blockType)
mc.setBlock(x + 1, y + 2, z, blockType)
mc.setBlock(x - 1, y + 2, z, blockType)
mc.setBlock(x , y + 2, z - 1, blockType)
mc.setBlock(x , y + 2, z + 1, blockType)
mc.setBlock(x + 1, y, z, blockType)
mc.setBlock(x - 1, y, z, blockType)
mc.setBlock(x , y, z - 1, blockType)
mc.setBlock(x , y, z + 1, blockType)
mc.setBlock(x + 1, y + 1, z + 1, blockType)
mc.setBlock(x - 1, y + 1, z - 1, blockType)
mc.setBlock(x + 1, y + 1, z + 1, blockType)
mc.setBlock(x - 1, y + 1, z - 1, blockType)
mc.setBlock(x + 1, y + 2, z + 1, blockType)
mc.setBlock(x - 1, y + 2, z - 1, blockType)
mc.setBlock(x + 1, y + 2, z - 1, blockType)
mc.setBlock(x - 1, y + 2, z + 1, blockType)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 0
y = 3
z = 28
up = 1
blockType = 103
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + up, z, blockType)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
pos = mc.player.getPos()
x = pos.x - 5
y = pos.y - 3
z = pos.z - 5
width = 10
height = 2
length = 10
blockType = 103 # melon
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)

blockType = 8 # water
width = 8
height = 1
length = 8
air = 0
mc.setBlocks(x + 1, y + 1, z + 1, x + 1 + width, y + 1 + height, z + 1 + length, blockType)
# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
pos = mc.player.getPos()
x = pos.x - 5
y = pos.y - 3
z = pos.z - 5
width = 10
height = 2
length = 10
blockType = 41 # melon
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

height = 2
blockType = 41

# Spire sides: should be the same as height
sideHeight = height
mc.setBlocks(x + 1, y, z + 1, x + 3, y + sideHeight - 1, z + 3, blockType)

# Spire point: should be two times the height
pointHeight = 4
mc.setBlocks(x + 2, y, z + 2, x + 2, y + pointHeight - 1, z + 2, blockType)

# Spire base: should be half the height
baseHeight = 1
mc.setBlocks(x, y, z, x + 4, y + baseHeight - 1, z + 4, blockType)
# %%
wheat = 4 ** 3

# %%
mooshroom = 5 * 2 - 1 + 4 / 2

# %%
zombiePigmen = 6 * 3 - 2
# %%
zombiePigmen = 6 * (3 - 2)

# %%
sheep = 6
sheep += 5

# %%
import random
diceValue = random.randint(1, 6)

# %%
import random
score = 0
score += random.randint(0, 99)
points = random.randint(-99, 99)

# %%
x = va

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x = x + random.randint(-500, 500)
blockType = 103
mc.setBlocks(x, y - 1, z, blockType)
mc.player.setPos(x, y, z)

# %%
"Look out! There's a zombie behind you!"

"Welcome to my secret base!"

print("String")
print("chocolate")
chocolate
name = "Steve the Miner"
print(name)
Steve the Miner
input("What is your name? ")
What is your name? Craig
'Craig'
print(name)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
message = "This is the default message."
mc.postToChat(message)

time.sleep(5)
mc.postToChat(message)

# %%
firstName = "Charles"
lastName = "Laforte"
print(firstName + lastName)
print(firstName + " " + lastName)
print(firstName, lastName)
print("My name is " + firstName + " " + lastName)

# %%
print("My not-so-secret golden apple stash: " + str(myGoldenApples))
print(str(19) + str(84))
print("The year is " + str(19) + str(84))

# %%
username = input("Please enter a username: ")
message = input("Enter your message: ")
mc.postToChat(message)

# %%
cansOfTunaPerCat = 4
cats = imput("How many cats do you have? ")
cats = int(cats)
dailyTunaEaten = cats * cansOfTunaPerCat
cats = int(input("How many cats do you have? "))
dailyTunaEaten = cats * cansOfTunaPerCat


# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
blockType = 117 # Add imput() function here
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)



# %%
blockType = int(input("Enter a blockType: "))

# %%
try:
    noOfSunglasses = int(input("How many sunglasses do you own?"))
except:
    print("Invalid input: please enter a number")

# %%
mc.setBlock(x, y , z, blockType)

# %%
try:
    blockType = int(input("Enter a blockType: "))
    mc.setBlock(x, y, z, blockType)
except:
    mc.postToChat("You did not enter a number! Enter a number next time.")

# %%
import time #Place this somewhere near the top of your program
time.sleep(30)  #Makes the program wait 30 seconds

# %%
import time
import math
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

time.sleep(2)

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

#Compare the difference between the starting position and ending position
dx = x2 - x1
dy = y2 - y1
dz = z2 - z1

distance = math.sqrt(dx*dx + dy*dy + dz*dz)

#Post the results to the chat
mc.postToChat("The player moved a distance of " + str(distance) + " blocks away.")
# %%
import math
math.sqrt(65)

x = 9
y = 2
z = 5
# %%
light = True
light = False

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

mc.setting("world_immutable", True)

# %%
agree = True
print("I agree: " + str(agree))
I agree: True

# %%
length = 2
width = 2
length == width
True



# %%
blockType = mc.getBlock(10, 18, 13)

# %%
from mcpi.minecraft import minecraft
mc = Minecraft.create("smalldell1")

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
mc.postToChat(blockType == 0)


# %%
width = 3
length = 2
width != length
True

# %%
width = 3
length = 3
width != length

# %%
notAir = blockType == 0
mc.postToChat("The player is not standing in air: " + str(notAir))


# %%
limit = 100
obsidian = 99
limit > obsidian
True

# %%
limit = 100
obsidian = 100
canLift = limit > obsidian
False

# %%
vanHeight = 8
bridgeHeight = 12
vanHeight < bridgeHeight
True

# %%
vanHeight = 8
bridgeHeight = 7
vanHeight < bridgeHeight
False

# %%
stickers = 30
people = 30
stickers >= people
True

# %%
stickers = 30
people = 31
stickers >= people
False

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x, z)
mc.postToChat(highestBlockY)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
import math
homeX = 10
homeZ = 10
pos = mc.player.getTilePos()
x = pos.x
z = pos.z
distance = math.sqrt((homeX - x) ** 2 + (homeZ - z) ** 2)
mc.postToChat(distance)

# %%
age = 21
ownsCar = True
age > 18 and ownsCar == True
# %%
age = 25
ownsCar = False
age > 18 and ownsCar == True

# %%
catColor = input("What color is the cat?")
myCatNow = catColor == "black" or catColor == "orange"
print("Adopt this cat: " + str(myCatNow))

# %%
not True
False

not False
True
hungry = False
sleepy  =True
timeForBed = not hungry and sleepy
print(timeForBed)
True

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

x = 10
y = 11
z = 12
melon = 42
block = mc.getBlock(x, y, z)

noMelon = # Check the block is not a melon

nmc.postToChat("You need to get some food: " + str(noMelon))

# %%
wolves = input("Enter the number of wolves: ")
enoughWolves = wolves > 10 and wolves < 20
print("Enough wolves: " + str(enoughWolves))

# %%
from mcpi.minecraft import Minecraft
mc = minecraft.create("smalldell1")

buildX =
buildY = 
buildZ =
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < build + width and
# %%
zombies = int(input("Enter the number of zombies: "))
if zombies > 20:
    print("That's a lot of zombies.")

# %%
password = "cats"
attempt = input("Please enter the password: ")
if attempt == password:
    print("Password is correct")
print("Program finished")

# %%
from mci.minecraft import Minecarft
mc = Minecarft.create("smalldell1")

answer = input("Create a creater? Y/N ")

# Add an if statement here

pos = mc.player.getPos()
mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
mc.postToChat("Boom.")

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z)

# if gift is a diamond block
if

# else if gift is a sapling
elif 

else:
    mc.postToChat("Bring a gift to " + str(x) + ", " + str(y) + ", " + str(z))

# %%
zombies = int(input("Enter the number of zombies: "))
if zombies > 20:
    print("Aahhh. Zombies.")
elif zombies > 10:
    print("There's just half a Minecraft apocalypse.")
elif zombies == 0:
    print("No zombies here!")
else:
    print("You know, you zombies aren't so bad.")

# %%
cakes = int(input("Enter the number of cakes to buy: "))
if 0 < cakes < 30:
    print("Here are your " + str(cakes) + " cakes.")
elif cakes == 0: 
    print("Don't you want some delicious cake?")
else:
    print("That's too many cakes! Don't be selfish!")

# %%
bread = int(input("Enter the amount of bread: "))
if not 20 <= bread <= 30:
    print("Here are your " + bread + " breads.")
else:
    print("I don't sell that amount of bread for a reason.")

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
valid = True

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if not -127 < x < 127:
    valid = False

# Check if y is not between -63 and 63

# Check if z is not between -127 and 127

if valid:
    mc.player.setPos(x, y, z)
else:
    mc.postToChat("Please enter a valid location")

# %%
hasCake = input("Do you have any cake? Y/N")
wouldShare = input("Would you give me some cake? Y/N")

if hasCkae == "Y" and wouldShare == "Y":
    print("Yay!")
else:
    print("Boo!")
# %%
hasCake = input("Do ou have any cake? Y/N")
wouldShare = input("Would you give me some cake? Y/N")

if hasCake == "Y" or wouldShare == "Y":
    print("Yay!")
else:
    print("Boo!")

# %%
wearingShoes = input("Are you wearing shoes? Y/N")
if not wearingShoes == "Y":
    print("You're not wearing shoes!Phufufufu!")

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

shwrX = 
shwrY = 
shwrZ = 

width = 5
height = 5
length = 5

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x <= shwrX + width and
    mc.setBlocks(shwrX, shwrY + height, shwrZ,
                shwrX + width, shwrY + height, shwrZ + length, 8)
else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ,
                shwrX + width, shwrY + height, shwrZ + length, 0)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y, pos.z, 8)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
import time

score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

# Add a while loop here
time.sleep(1)
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
score = score + 1
mc.postToChat("Current score: " + str(score))

mc.postToChat("Final score: " + str(score))

if score > 6:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38
                
# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
import time

pos = mc.player.getTilePos()
floorX = pos.x – 2
floorY = pos.y - 1
floorZ = pos.z – 2
width = 5
length = 5
block = 41

mc.setBlocks(floorX, floorY, floorZ,
floorX + width, floorY, floorZ + length, block)

while floorX <= pos.x <= floorX + width and # Check z is within the floor
    if block == 41:
    block = 57
    else:
    block = 41
    mc.setBlocks(floorX, floorY, floorZ,
                floorX + width, floorY, floorZ + length, block)
    pos = mc.player.getTilePos()
    time.sleep(0.5)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

air = 0
water = 9

# Add and infinite while loop here
    pos = mc.player.getTilePos()
    blokcBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

    # Add if statement here
        mc.setBlock(pos.x, pos.y - 1, pos.z, 41)

# %%
from mcpi.minecraft import Minecraft
import math
import time
import random
mc = Minecraft.create("smalldell1")

destX = random.randint(-127, 127)
destZ = random.randint(-127, 127)
destY = mc.getHeight(destX, destZ)

block = 57
mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Block set")

while True:
    pos = mc.player.getPos()
    distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)

    if distance > 100:
        mc.postToChat("Freezing")
    elif distance > 50:
        mc.postToChat("Cold")
    elif distance > 25:
        mc.postToChat("Warm")
    elif distance > 12:
        mc.postToChat("Boiling")
    elif distance > 6:
        mc.postToChat("On fire.")
    elif distance == 0:
        mc.postToChat("Found it")

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

def growTree(x, y, z):
    # Creates a tree at the coordinates given
    # Write your code to make a tree here

pos = mc.player.getTilePos
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import time

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y -1, z, 103)
time.sleep(10)

pos = mc.player.getPos()
x = pos.x
y = pos.y - 1
z = pos.z
mc.setBlock(x, y, z, 103)
time.sleep(10)

pos = mc.player.getPos()
x = pos.x
y = pos.y - 1
z = pos.z
mc.setBlock(x, y, z, 103)
time.sleep(10)

# %%
priceOfCookie = calculateCookiePrice(6) # Value will be 80

# %%
def numberOfChickens():
    return 5

coop = numberOfChickens()
print(numberOfChickens)

# %%
extraChickens = 4 + numberOfChickens # Value of 9

# %%
def chickenNoise():
    print("Cluck")

chickenNoise()

# %%
def chickenNoise():
    return "Cluck"

multipleNoises = chickenNoise() + ", Bork"
print(multipleNoises)

# %%
def melon():
    """ Returns the value of the melon block """
    return 103

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

# Functions go here 

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

# Functions go here 

block = diamond()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)

# %%
def wordToNumber(numToConvert):
    """ Converts a number written as a word to an integer """
    if numToConvert == "one":
        numAsInt = 1
    elif numToConvert == "two":
        numAsInt = 2
    elif numToConvert == "three":
        numAsInt = 3
    elif numToConvert == "four":
        numAsInt = 4
    elif numToConvert == "five":
        numAsInt = 5

    return numAsInt

# %%
def chooseGreeting(metBefore):
    """ Chooses a greeting depending on whether you've met someone before.
    metBefore argument should be a Boolean value """
    if metBefore:
        print("Nice to see you again")
    else:
        print("Nice to meet you")

chooseGreeting(True)
chooseGreeting(False)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

block = 36
state = 6
# Creates a single block of pink wool
mc.setBlock(10, 3, -4, block, state)

# Creates a cuboid of pink wool
mc.setBlocks(11, 3, -4, 20, 6, -8, block, state)

# %%
def getWoolState(color):
    """ Takes a color as a string and returns the wool block state for that color """
    if color == "pink":
        blockState = 6
    elif # Add elif statements for the other colors
    # Return the blockState here

colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")
import random

def randomBlockLocatinos(blockType, repeats):
    count = 0
    # Add the loop here
    x = random.randint(-127, 127)
    z = random.randint(-127, 127)
    y = mc.getHeight(x, z)
    mc.setBlock(x, y, z, blockType)
    count += 1

# %%
eggs = 12

def increaseEggs():
    eggs += 1
    print(eggs)

increaseEggs()

# %%
eggs = 12

def increaseEggs():
    global eggs
    eggs += 1
    print(eggs)

increaseEggs()

# %%
eggs = 12

def increaseEggs():
    eggs = 0
    eggs += 1
    print(eggs)

increaseEggs()
print(eggs)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import time

def claculateMove():
    """ Changes the x and z variables for a block. If the block in front of the block is less than 2 blocks higher, it will move forward; otherwise it will try to move left, then backward, then finally right. """
    # Create global variables here

    currentHeight = mc.getHeight(x, z) - 1

    forwardHeight = mc.getHeight(x + 1, z)
    rightHeight = mc.getHeight(x, z + 1)
    backwardHeight = mc.getHeight(x - 1, z)
    leftHeight = mc.getHeight(x, z - 1)

    if forwardHeight - currentHeight < 3:
        x += 1
    elif rightHeight - currentHeight < 3:
        z += 1
    elif leftHeight - currentHeight < 3:
        z -= 1
    elif backwardHeight - currentHeight < 3:
        x -= 1

    y = mc.getHeight(x, z)

pos = mc.player.getTilePos()
x = pos.x
z = pos.z
y = mc.getHeight(x, z)

while True:
    # Claculate block movement
    calculateMove()

    # Place block
    mc.setBlock(x, y, z, 103)

    # Wait
    time.sleep(1)

    # Remove the block
    mc.setBlock(x, y, z, 0)

# %%
from mcpi.minecrft import Minecraft
mc = Minecraft.create("smalldell1")

import time

heights = [100, 0]
count = 0

while count < 60:
    pos = mc.player.getTilePos()

    if pos.y < heights[0]:
        # Set the lowest height to the y variable
    elif pos.y > heights[1]:
        # Set the hightest height to the y variable

    count += 1
    time.sleep(1)

mc.postToChat("Lowest: ") # Output lowest height
mc.postToChat("Highest: ") # Output highest height

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import time

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

# Add 10 glass blocks (ID 20) to this empty list
block = [ ]
barBlock = 22 # Lapis Lazuli

count = 0
while count <= len(blocks):
    
    mc.setBlock(x, y, z, blocks[0])
    mc.setBlock(x, y + 1, z, blocks[1])
    mc.setBlock(x, y + 2, z, blocks[2])
    # Add setBlock() for the remaining blocks in the list

    count += 1

    # Delete the last block in the list

    #Insert a lapis lazuli block at the first position in the list

    time.sleep(2)

# %%
flavor = "Grape"
print(flavor[1])

firstName = "Lyra"
lastName = "Jones"
initials = firstName[0] + " " + lastNAme[0]
print(initials)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import random
import time

#%%

# Get the player's position

# Set the x, y, and z variables on the same line using a tuple

while True:
    x += random.uniform(-0.2, 0.2)
    # Change the z variable by a random float
    z += random.uniform(-63, 63)
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)

# %%
blockHits = mc.events.pollBlockHits()
mc.postToChat(f"blockHits={blockHits}")
time.sleep(10)
mc.postToChat(f"blockHits={blockHits}")

# %%
cake = ["Eggs",
        "Butter",
        "Sugar",
        "Milk",
        "Flour"]

# Store the list in a second variable
chocolateCake = cake[:]
chocolateCake.append("Chocolate")
# %%
cake = ["Eggs", "Butter", "Sugar", "Milk", "Flour"]
print("Eggs" in cake)
# %%
cake = ["Egsg", "Butter", "Sugar", "Milk", "Flour"]
if "Ham" in cake:
    print("That cake sounds disgusting.")
else:
    print("Good. Ham in a cake is a terrible mistake.")

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import time

blocks = []

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        hitX, hitY, hitZ = hit.pos.x, hit.pos.y, hit.pos.z1
        block = mc.getBlock(hitX, hitY, hitZ)
        blocks.append(block)

    # Add the if statement here
    time.sleep(0.2)

# %%
places = {'Living room': (76, 1, -61), 'Bedroom': (6 1, 9, -61)}

# %%
location = places{'Living room'}
x, y, z = loction[0], location[1], location[2]

# %%
from mcpi.minecraft import Minecraft
mc = Minecarft.create("smalldell1")

# Add locations to the dictionnary
places = {}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit to close): ")
    if choice in places:
        # Store the dictionary item's value using it's key (choice)
        location = 
        # Store the values stored in the tuple in the x, y, and z variables
        x, y, z = 
        mc.player.getTilePos(x, y, z)

# %%
person['age']


# %%
mc.postToChat("Papa is a fucking idiot!He thinks that my brain can hold anything.")


# %%
# Question 1: How do you post something to the chat?
# Answer: mc.postToChat("")

# Question 2: Can you manipulate a list?
# Answer: Yes

# Question 3: How do you delete an item of your list?
# Answer: del

# Question 4: How do you print something?
# Answer: print()

# Question 5: How do you defINE A VARIABLE?
# blabla = "gougou"

# Question 6: How do you use a tuple in one line?
# Ex: x, y, z = 10, 11, 12 

# Question 7: How do you import something?
# Examples: import math, import random, import Minecraft

# Question 8: How do you make the computer wait?
# Answer: time.sleep()

# Question 9: Is True a boolean value?
# Answer: Yes

# Question 10: What is else and if together
# Answer: elif

# Question 11: What is an integer?
# Answer: A full number

# Question 12: What is a float?
# Answer: A number with a dot 

# Question 13: How do you add a note?
# Answer: By clicking shift and 3

# Question 14: What does break mean?
# Answer: Getting out of a loop

# Question 15: What happens if you put a : at the end of a line?
# Answer: it will move a few spaces away like if you press the tab key

# %%
# page 194

# %%
person['age'] = 43

# %%
person['location'] = 'USS Discovery'

# %%
# Connect to the Minecraft game
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import time

name = ""
scoreboard = {}

while True:
    # Get the player's name
    name = input("What is your name? ")
    # Break loop if name is exit 
    if name == "exit":
        break
    mc.postToChat("Go!")

    # Wait 60 seconds
    time.sleep(60)

    # Get the list of block hits
    blockHits = mc.events.pollBlockHits()

    # Display the length of the block hits list to chat
    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))

    # Add the player to the scoreboard

    # Display the scoreboard
    print(scoreboard)

    7 

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import time

time.sleep(60)

hits = mc.events.pollBlockHits()
block = 103

for
x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
# Set melon blocks at the coordinates
# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

stairBlock = 53

step = 0
while step < 10:
    mc.setBlock(x + step, y + step, z, stairBlock)
    step += 1

# %%
aRange = range(5)
list(aRange)

# %%
aRange = range(2.5)
list(aRange)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

def setPillar(x, y, z, height):
    """ Creates a pillar. Args set position and height of pillar """
    print(x, y, z, height)
    stairBlock = 156
    block = 155

    # Pillar top
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, block, 1)
    mc.setBlock(x - 1, y + height - 1, z, stairBlock, 12)
    mc.setBlock(x + 1, y + height - 1, z, stairBlock, 13)
    mc.setBlock(x, y + height - 1, z + 1, stairBlock, 15)
    mc.setBlock(x, y + height - 1, z - 1, stairBlock, 14)

    # Pillar base
    mc.setBlock(x - 1, y, z - 1, x + 1, y, z + 1, block, 1)
    mc.setBlock(x - 1, y + 1, z, stairBlock, 0)
    mc.setBlock(x + 1, y + 1, z, stairBlock, 1)
    mc.setBlock(x, y + 1, z + 1, stairBlock, 3)
    mc.setBlock(x, y + 1, z - 1, stairBlock, 2)

    # Pillar column
    mc.setBlocks(x, y, z, x, y + height, z, block, 2)

#%%
pos = mc.player.getTilePos()
x, y, z = pos.x + 2, pos.y, pos.z

#%%
setPillar(x, y, z, 10)

setPillar(x - 10, y, z, 10)

setPillar(x - 20, y, z, 10)

setPillar(x - 30, y, z, 10)

setPillar(x - 40, y, z, 10)

setPillar(x - 50, y, z, 10)

setPillar(x - 60, y, z, 10)
#%%
for j in range(0, 95, 5):
    setPillar(x + j, y, z, 15)    

# %%
for j in range(3, 13, 3):
    print(j)
#%%

# Add the for loop here
setPillar(range(0, 5, 5))
# Call the function here
print(setPillar)
# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

block = 24 # sandstone
height = 10
levels = range(height)

pos = mc.player.getTilePos()
x, y, z = pos.x + height, pos.y, pos.z

for level in levels:
    mc.setBlocks(x - level, y, z - level, x + level, y, z + level, block)
    y += 1

# %%
print(scoreboard)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

oneDimensionalRainbowList = [0, 1, 2, 3, 4, 5]


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for color in oneDimensionalRainbowList:
    mc.setBlock(x, y, z, 35, color)
    y += 1

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

twoDimensionalRainbowList = [[0, 0, 0],
                             [1, 1, 1],
                             [2, 2, 2],
                             [3, 3, 3],
                             [4, 4, 4],
                             [5, 5, 5]]
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

startingX = x

for row in twoDimensionalRainbowList:
    for color in row:
        mc.setBlock(x, y, z, 35, color)
        x += 1
    y += 1
    x = startingX

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

pos= mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

blocks = [[35, 35, 35, 35, 35, 35, 35, 35],
          [35, 35, 35, 35, 35, 35, 35, 35],
          [35, 35, 35, 35, 35, 35, 35, 35],
          [35, 35, 35, 35, 35, 35, 35, 35]]

for row in reversed(blocks):
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x


# %%

# %%
import random
randomNumbers = []
for outer in range(10):
    randomNumbers.append([])
    for inner in range(10):
        number = random.randint(1, 4)
        randomNumbers[outer].append(number)
print(randomNumbers)

# %%
[[3, 1, 4, 1, 4, 1, 2, 3, 2, 2],
 [1, 3, 4, 2, 4, 3, 4, 1, 3, 2],
 [4, 2, 4, 1, 4, 3, 2, 3, 4, 4],
 [1, 4, 3, 4, 3, 4, 3, 3, 4, 4],
 [3, 1, 4, 2, 3, 3, 3, 1, 4, 2],
 [4, 1, 4, 2, 3, 2, 4, 3, 3, 1],
 [2, 4, 2, 1, 2, 1, 4, 2, 4, 3],
 [3, 1, 3, 4, 1, 4, 2, 2, 4, 1],
 [4, 3, 1, 2, 4, 2, 2, 3, 1, 2],
 [3, 1, 3, 3, 1, 3, 1, 4, 1, 2]]

# %%
from mcpi.miencraft import Minecraft
mc = Minecraft.create("smalldell1")

import random

def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z1

brokenWall = []
height, width = 5, 10

# Create the list of broken blocks

# Set the blocks

# %%
cube = [[[57, 57, 57, 57],
[57, 0, 0, 57],
[57, 0, 0, 57],
[57, 57, 57, 57]],
#
[[57, 0, 0, 57],
[0, 0, 0, 0],
[0, 0, 0, 0],
[57, 0, 0, 57]],
#
[[57, 0, 0, 57],
[0, 0, 0, 0],
[0, 0, 0, 0],
[57, 0, 0, 57]],
#
[[57, 57, 57, 57],
[57, 0, 0, 57],
[57, 0, 0, 57],
[57, 57, 57, 57]]]

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
cube = [[[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]],
[[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
[[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
[[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]]]
startingX = x
startingY = y

for depth in cube:
    for height in reversed(depth):
        for block in height:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = startingX
    z += 1
    y = startingY

# %%
[[57, 57, 57, 57],
 [57, 0, 0, 57],
 [57, 0, 0, 57],
 [57, 57, 57, 57]]
 
# %%
[[57, 0, 0, 57],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [57, 0, 0, 57]]

# %%
[[57, 0, 0, 57],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [57, 0, 0, 57]]

# %%
[[57, 57, 57, 57],
 [57, 0, 0, 57],
 [57, 0, 0, 57],
 [57, 57, 57, 57]]

# %%
cube = [[[57, 57, 57, 57],
         [57, 0, 0, 57],
         [57, 0, 0, 57],
         [57, 57, 57, 57]],
         #
        [[57, 0, 0, 57],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [57, 0, 0, 57]],
         #
        [[57, 0, 0, 57],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [57, 0, 0, 57]],
         #
        [[57, 57, 57, 57],
         [57, 0, 0, 57],
         [57, 0, 0, 57],
         [57, 57, 57, 57]]]

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
    #Sort the highest and lowest x, y, and z variables
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    structure = []

    print("Please wait...")

    # COpy the structure

    return structure
def buildStructure(x, y, z, structure):
    xStart = x
    yStart = y

    # BUild the structure

# Get the position of the first corner
input("Move to the first corner and press enter in this window")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z
# Get the position of the second corner
input("Move to the opposite corner and press enter in this window")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z
# Copy the building
structure = copyStructure(x1, y1, z1, x2, y2, z2)
# Set the position for the copy
input("Move to the position you want to create the structure and press ENTER 
in this window")
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
buildStructure(x, y, z, structure)

# %%
secretFile = open("secretFile.txt", "w")

# %%
secretFile = open("/secrets/secretFile.txt", "w")

# %%
secretFile = open("secretFile.txt", "w")
secretFile.write("This is a secret file. Shhh! Don't tell anyone.")
secretFile.close()

# %%
secretFile = open("secretFile.txt", "r")

print(secretFile.read())
secretFile.close()

# %%
secretFile = open("secretFile.txt", "r")

print(secretFile.readline())
print(secretFile.readline())
print(secretFile.readline())

secretFile.close()

# %%
toDoFile = 

toDoList = ""

toDoItem = input("Enter a to-do list item: ")

while toDoItem != "exit":
    toDoList = toDoList + toDoItem + "n\"
    toDOItem = input("Enter a to-do list item: ")

# Write the to-do list to the file
# Close the file

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

toDoList = 

for line in toDoList:
    # Output "line" to the chat
# %%
from pickle import dump

locations = {'Jhon': 'Forest', 'Phillipa': 'Mountains', 'Pete': 'City'}

secretFile= open("secretFile", "wb")
dump(locations, secretFile)

# %%
from pickle import *
locations = {'Jhon': 'Forest', 'Phillipa': 'Mountains', 'Pete': 'City'}

secretFile= open("secretFile", "wb")
dump(locations, secretFile)

locations = load(secretFile)
print(locations['Phillipa'])

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import pickle
def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z1 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    structure = []

    print("Please wait...")

     # Copy the structure
     for row in range(height):
         structure.append([])
         for column in range(width):
            structure[row].append([])
            for depth in range(length):
                block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
                structure[row][column].append(block)

        return structure

# Get the position of the first corner
input("Move to the first position and press ENTER in this window")
pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

# Get the position of the second corner
input("Move to the opposite corner and press ENTER in this window")
pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

structure = copyStructure( x1, y1, z1, x2, y2, z2)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import pickle

def buildStructure(x, y, z, structure):
    xStart = x
    yStart = y
    for row in structure:
        for column in row:
            for block in column:
                mc.setBlocks(x, y, z, blck.id, block.data)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart

# Open and load the structure file
structure = 

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
buildStructure(x, y, z, structure)

# %%
import pickle 

-- snip --

# Name the structure
structureName = input("What do you want to call the structure?")

# STore the strucuture in a file
pickleFile = open("pickleFile", "wb")
pockleFile.dump(structure)

# %%
import pickle

--snip--

structure = pickle.load("pickleFile")
strcutureName = input("Enter the structure's name")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

buildStructure(x, y, z, strcutureDictionary[structureName])

# %%
from flask import Flask
app = Flask(__name__)

@app.route("/")
def showName():
    return "Craig Richardson"

app.run

# %%
class ClassName(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

# %%
class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

fluff = Cat("Fluff", 4.5)

print(fluff.weight)

# %%
fluff.weight = 5
# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

class Location(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

bedroom = Location(64, 52, -8)
mc.player.getTilePos(bedroom.x, bedroom.y, bedroom.z)

# %%
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

import time

class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

    def build(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + self.width, self.y + self.height, self.z + self.depth, 4)

        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1, self.x + self.width - 1, self.y + self.height - 1, self.z + depth - 1, 0)

    def clear(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + self.width, self.y + self.height, self.z + self.depth, 0)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ghostHouse = Building(x, y, z, 10, 6, 8)
ghostHouse.build()

time.sleep(30)

ghostHouse.clear()
ghostHouse.x = 8

# %%
from mcpi.minecraft import Minecraft
mc = miencraft.create("smalldell1")

import time

class NamedBuilding(object):
    def __init__(self, x, y, z, width, height, depth, name):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

        self.name = name

    def build(self):
        mc.setBlocks(self.x, self.y, self.z,
        self.x + self.width, self.y + self.height,
        self.z + self.depth, 4)

        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1,
        self.x + self.width - 1, self.y + self.height - 1,
        self.z + self.depth - 1, 0)
    def clear(self):
        mc.setBlocks(self.x, self.y, self.z,
        self.x + self.width, self.y + self.height,
        self.z + self.depth, 0)

    def getInfo():

pos = mc.player.getTilePos():
x = pos.x 
y = pos.y
z = pos.z
ghostCastle = NamedBuilding(x, y, z, 10, 16, 16, "Ghost Castle")
ghostCastle.build()
mc.postToChat(ghostCastle.getInfo())

time.sleep(30)

ghostCastle.clear()

# %%
def (object)

ghostHouse = Building(17, 22, -54, 10, 6, 8)
ghostHouse.build()
time.sleep(30)
ghostHouse.clear()
# %%
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
ghostHouse = Building(x, y, z, 10, 6, 8)
shop = Building(x + 12, y, z, 8, 12, 10)
# Create more ghost building objects here
ghostHouse.build()
shop.build()
# Build more ghost building objects here
time.sleep(30)
ghostHouse.clear()
shop.clear()
# %%
class Cat(object):
owner = "Craig"
def __init__(self, name, weight):
self.name = name
self.weight = weight
def eat(self, food):
self.weight = self.weight + 0.05
print(self.name + " is eating " + food)
def eatAndSleep(self, food):
self.eat(food)
print(self.name + " is now sleeping...")
def getWeightInGrams(self):
return self.weight * 1000
fluff = Cat("Fluff", 4.5)
print(fluff.owner)
stella = Cat("Stella", 3.9)
print(stella.owner)
print(fluff.weight)
fluff.eat("tuna")
fluff.eatAndSleep("tuna")
print(fluff.getWeightInGrams())
print(fluff.name)
print(stella.name)
fluff.eat("tuna")
stella.eat("cake")
stella.owner = "Matthew"
print(stella.owner)
print(fluff.owner)
# %%
# Create a FancyBuilding class here
def upgrade(self):
# Carpet
mc.setBlocks(self.x + 1, self.y, self.z + 1,
self.x + self.width - 1, self.y, self.z + self.depth - 1,
35, 6)
# Flowers
mc.setBlocks(self.x - 1, self.y, self.z -1,
self.x - 1, self.y, self.z + self.depth + 1,
37)
mc.setBlocks(self.x - 1, self.y, self.z - 1,
self.x + self.width + 1, self.y, self.z – 1,
37)
mc.setBlocks(self.x + self.width + 1, self.y, self.z - 1,
self.x + self.width + 1, self.y, self.z + self.depth + 1,
37)
mc.setBlocks(self.x - 1, self.y, self.z + self.depth + 1,
self.x + self.width + 1, self.y, self.z + self.depth = 1,
37)
# Create an instance of the FancyBuilding class
# Call the build() and upgrade() methods

# %%
class Bird(object):
def __init__(self, name, wingspan):
self.name = name
self.wingspan = wingspan
def birdcall(self):
print("chirp")
def fly(self):
print("flap")
class Penguin(Bird):
def swim(self):
print("swimming")
def birdcall(self):
print("sort of a quack")
def fly(self):
print("Penguins cannot fly :(")
class Parrot(Bird):
def __init__(self, name, wingspan, color):
self.name = name
self.wingspan = wingspan
self.color = color
gardenBird = Bird("Geoffrey", 12)
gardenBird.birdcall()
gardenBird.fly()
sarahThePenguin = Penguin("Sarah", 10)
sarahThePenguin.swim()
sarahThePenguin.fly()
sarahThePenguin.birdcall()
freddieTheParrot = Parrot("Freddie", 12, "blue")
print(freddieTheParrot.color)
freddieTheParrot.fly()
freddieTheParrot.birdcall()

# %%
class Penguin(Bird):
    def swim(self):
        print(swimming)

# %%
sarahThePenguin = Penguin("Sarah", 10)
sarahThePenguin.swim()

# %%
sarahThePenguin.fly()
sarahThePenguin.birdcall()

# %%
from mcpi.minecraft import Minecraft
mc = Miencraft.create("smalldell1")

# Paste the ghostHouse.py program here
# Create a Tree class here

def growTree(x, y, z):
    """ Creates a tree at the coordinates given """
    wood = 17
    leaves = 18

    # Trunk
    mc.setBlocks(x, y, z, x, y + 5, z, wood)

    # Leaves
    mc.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, leaves)
    mc.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, leaves)

# Create build() and clear() methods for the Tree class here

# %%
n = 8
is_odd = (n % 2) == 1

if is_odd:
    print("Weird")
else:
    print("Not Weird")

# %%