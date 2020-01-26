# Create an empty set named showroom.
# Add four of your favorite car model names to the set.
# Print the length of your set.
# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
# Using update(), add two more car models to your showroom with another set.
# You've sold one of your cars. Remove it from the set with the discard() method.
# Acquiring more cars
# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

showroom = set()

showroom = { 'mini cooper', 'kia rio', 'honda accord', 'numbus 2000' }
print(len(showroom))
# len(showroom)

showroom.add('mini cooper')

new_cars =set()

new_cars = {'truck', 'jeep'}

showroom.update(new_cars)

showroom.discard("truck")
showroom.discard("jeep")

junkyard = set()

junkyard = {'toyota pickup', 'mazda miata', 'flinstone', 'mini cooper', 'kia rio'}

duplicate_inventory = showroom.intersection(junkyard)
# intersection method shows you what you have in common in 2 different sets, (i.e. do i have coopers in both my showroom and my junk yard? intersection!)

print(duplicate_inventory)


showroom = showroom.union(junkyard)
# union() similar to add()


showroom.discard('honda accord')
print(showroom)




