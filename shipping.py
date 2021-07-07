
# weight = 41.5
# weight = 8.4
# weight = 1.5
# weight = 4.8
weight = 41.5

# Ground Shipping
if weight <= 2:
  cost_ground_shipping = (weight * 1.5) + 20
elif weight <= 6:
  cost_ground_shipping = (weight * 3) + 20
elif weight <= 10:
  cost_ground_shipping = (weight * 4) + 20
else:
  cost_ground_shipping = (weight * 4.75) + 20

print("Cost of Ground Shipping a package of weight", weight, "= $", cost_ground_shipping)

# Ground Shipping Premium
cost_ground_premium = 125.00
print("Cost of Ground Shipping Premium = $", cost_ground_premium)


# Drone Shipping
if weight <= 2:
  cost_drone_shipping = weight * 4.5
elif weight <= 6:
  cost_drone_shipping = weight * 9
elif weight <= 10:
  cost_drone_shipping = weight * 12
else:
  cost_drone_shipping = weight * 14.25

print("Cost of Drone Shipping a package of weight", weight, "= $", cost_drone_shipping)


# Solution
# For a 4.8 pound package, Looking at the results below, Ground Shipping is the cheapest ($ 34.4)

# Cost of Ground Shipping a package of weight 4.8 = $ 34.4
# Cost of Ground Shipping Premium = $ 125.0
# Cost of Drone Shipping a package of weight 4.8 = $ 43.199999999999996


# For a 41.5 pound package, Looking at the results below, Ground Shipping Premium is the cheapest ($ 125.0)

# Cost of Ground Shipping a package of weight 41.5 = $ 217.125
# Cost of Ground Shipping Premium = $ 125.0
# Cost of Drone Shipping a package of weight 41.5 = $ 591.375