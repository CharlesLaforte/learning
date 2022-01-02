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
count = 1
while count <= 5:
    print(count)
    count += 1
print("Loop finished")

# %%
import random 
from mcpi.minecraft import Minecraft
mc = Minecraft.create("smalldell1")

# Add the count variable here 
#Start the while loop here 
x = random.randint(-127, 127) # Indent the code from this line
y = random.randint(0, 64)
z = random.randint(-127, 127)

mc.player.setTilePos(x, y, z)
# Add 1 to the value of the count variable here