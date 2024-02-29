# Define a class to represent a character in a game

import random


class Character:
    """
    A class to represent a character in a game.
    """

    def __init__(self, pos_x=0, pos_y=0):
        """
        Initialize the character's position to the origin (0, 0).
        This code snippet is a Python class constructor that initializes the character's position to the origin (0, 0) with default values for the x and y coordinates. 
        However, it seems like the default values provided in the function signature are not being utilized, as the pos_x and pos_y attributes are being set to 0 directly.
        """
        self.pos_x = pos_x
        self.pos_y = pos_y

    # Method to move the character to the specified position
    def move(self, pos_x, pos_y):
        """
        Move the character to the specified position.

        :param pos_x: The x-coordinate of the new position.
        :param pos_y: The y-coordinate of the new position.
        """
        self.pos_x = pos_x
        self.pos_y = pos_y

    # Method to restart the character's position to the origin (0, 0)
    def restart(self):
        """
        Reset the character's position to the origin (0, 0).
        """
        self.pos_x = 0
        self.pos_y = 0

    # Method to calculate the distance between this character and another character
    def distance(self, other):
        """
        Calculate the distance between this character and another character.

        :param other: The other character.
        :return: The distance between the two characters.
        """
        return ((self.pos_x - other.pos_x) ** 2 + (self.pos_y - other.pos_y)
                ** 2) ** 0.5

    def random_movement(self, map_size):
        """
        Move the character to a random position on the map.

        :param map_size: The size of the map.
        """
        self.pos_x = random.randint(0, map_size - 1)
        self.pos_y = random.randint(0, map_size - 1)

# TODO Testing TODO plugin

######################## MAIN ########################


map_size = input("Enter the size of the map: ")

# Create instances of Character for the player and the enemy
player = Character()
enemy = Character()

# Print the positions of the player and the enemy
print(f"Player position: x = {player.pos_x}, y = {player.pos_y}")
print(f"Enemy position: x = {enemy.pos_x}, y = {enemy.pos_y}")

# Move the player and the enemy to specific positions
player.move(2, 4)
enemy.move(6, 8)

# Print the positions of the player and the enemy
print(f"Player position: x = {player.pos_x}, y = {player.pos_y}")
print(f"Enemy position: x = {enemy.pos_x}, y = {enemy.pos_y}")

# Print the distance between the player and the enemy
print("Distance between player and enemy: ", player.distance(enemy))

# Reset the positions of the player and the enemy to the origin
player.restart()
enemy.restart()

# Print the positions of the player and the enemy after resetting
print(f"Player position: x = {player.pos_x}, y = {player.pos_y}")
print(f"Enemy position: x = {enemy.pos_x}, y = {enemy.pos_y}")

# Print the distance between the player and the enemy after resetting
print("Distance between player and enemy: ", player.distance(enemy))

# Call the random_movement method for the player object with the map_size as an argument
player.random_movement(int(map_size))

# Call the random_movement method for the enemy object with the map_size as an argument
enemy.random_movement(int(map_size))

# Print the positions of the player and the enemy
print(f"Player position: x = {player.pos_x}, y = {player.pos_y}")
print(f"Enemy position: x = {enemy.pos_x}, y = {enemy.pos_y}")

# Print the distance between the player and the enemy using the distance method of the player object
print(f"Distance between player and enemy: {player.distance(enemy)}")

######################## END ########################

# FIXME Testing TODO plugin
# ? Testing TODO plugin
# ! Warning
# HACK Testing TODO plugin
