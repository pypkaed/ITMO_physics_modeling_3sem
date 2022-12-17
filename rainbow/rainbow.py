###############################################
#                  TASK INFO                  #
#                                             #
#    All calculations are to be made only     #
#        for red and purple colours           #
#  ------------------------------------------ #
#     To see the calculation of the needed    #
#     equations and the whole logic behind    #
#      solving the case, see the attached     #
#                  .pdf file.                 #
###############################################


from matplotlib import pyplot as plt
import math

# initialization:
refractive_index_red = 1.331
refractive_index_purple = 1.343
dy = 0.0001

y_list = []
phi1_red_list = []
phi1_purple_list = []
phi2_red_list = []
phi2_purple_list = []

I_red_phi1 = []
I_purple_phi1 = []
I_red_phi2 = []
I_purple_phi2 = []


# y > 0
def phi_1(y, refractive_index):
    return (4 * math.asin(y / refractive_index) - 2 * math.asin(y)) * 180 / math.pi


# y < 0
def phi_2(y, refractive_index):
    return (math.pi + 6 * math.asin(-y / refractive_index) - 2 * math.asin(-y)) * 180 / math.pi


def intensity(dphi):
    return dy / dphi


for y in range(0, 10000):
    y_list.append(y / 10000)

    angle = phi_1(y / 10000, refractive_index_red)      # phi_1 for red for this y
    phi1_red_list.append(angle)

    angle = phi_1(y / 10000, refractive_index_purple)   # phi_1 for purple for this y
    phi1_purple_list.append(angle)

    angle = phi_2(y / 10000, refractive_index_red)      # phi_2 for red for this y
    phi2_red_list.append(angle)

    angle = phi_2(y / 10000, refractive_index_purple)   # phi_2 for purple for this y
    phi2_purple_list.append(angle)


for i in range(len(phi1_red_list)):
    if i < len(phi1_red_list) - 1:
        angle = intensity(phi1_red_list[i + 1] - phi1_red_list[i])
        I_red_phi1.append(round(angle, 4))

for i in range(len(phi1_purple_list)):
    if i < len(phi1_purple_list) - 1:
        angle = intensity(phi1_purple_list[i + 1] - phi1_purple_list[i])
        I_purple_phi1.append(round(angle, 4))

for i in range(len(phi2_red_list)):
    if i < len(phi2_red_list) - 1:
        angle = intensity(phi2_red_list[i + 1] - phi2_red_list[i])
        I_red_phi2.append(round(angle, 4))

for i in range(len(phi2_purple_list)):
    if i < len(phi2_purple_list) - 1:
        angle = intensity(phi2_purple_list[i + 1] - phi2_purple_list[i])
        I_purple_phi2.append(round(angle, 4))

# graphs

print("Ir(phi1)max:", max(I_red_phi1), "Ir(phi1)min:", min(I_red_phi1))
print("Ip(phi1)max:", max(I_purple_phi1), "Ip(phi1)min:", min(I_purple_phi1))
print("Ir(phi2)max:", max(I_red_phi2), "Ir(phi2)min:", min(I_red_phi2))
print("Ip(phi2)max:", max(I_purple_phi2), "Ip(phi2)min:", min(I_purple_phi2))

print("Max reflection angle for red colour, y > 0:",
      round(phi1_red_list[I_red_phi1.index(max(I_red_phi1))], 4))
print("Max reflection angle for purple colour, y > 0:",
      round(phi1_purple_list[I_purple_phi1.index(max(I_purple_phi1))], 4))
print("Max reflection angle for red colour, y < 0:",
      round(phi2_red_list[I_red_phi2.index(max(I_red_phi2))], 4))
print("Max reflection angle for purple colour, y < 0:",
      round(phi2_purple_list[I_purple_phi2.index(max(I_purple_phi2))], 4))

plt.figure(figsize=(12, 8), dpi=300)
plt.grid()
plt.title("phi(y) for red and purple colours")
plt.ylabel("phi, rad")
plt.xlabel("y")
plt.plot(y_list, phi1_red_list, 'r', lw=3)
plt.plot(y_list, phi1_purple_list, 'm', lw=3)
plt.plot(y_list, phi2_red_list, 'r', lw=3)
plt.plot(y_list, phi2_purple_list, 'm', lw=3)
plt.show()

plt.figure(figsize=(12, 8), dpi=300)
plt.grid()
plt.title("I(phi) for red and purple colours")
plt.ylabel("I, Watt/m^2")
plt.xlabel("phi, rad")
plt.plot(phi1_red_list[0:9999], I_red_phi1, 'r', lw=3)
plt.plot(phi1_purple_list[0:9999], I_purple_phi1, 'm', lw=3)
plt.plot(phi2_red_list[0:9999], I_red_phi2, 'r', lw=3)
plt.plot(phi2_purple_list[0:9999], I_purple_phi2, 'm', lw=3)
plt.show()
