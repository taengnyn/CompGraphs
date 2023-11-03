import matplotlib.pyplot as plt

data_file = 'DS4.txt'

fig, ax = plt.subplots(figsize=(960/80, 540/80), dpi=80)
x = []
y = []
with open(data_file, 'r') as file:
    for line in file:
        x_coord, y_coord = map(float, line.strip().split())
        x.append(x_coord)
        y.append(y_coord)

ax.scatter(x, y, s=10, c='b', marker='o', label='Точки')

ax.set_xlabel('Вісь X')
ax.set_ylabel('Вісь Y')
ax.set_title('Графік точок з датасету')

ax.legend()

output_file = 'output_graph.png'
plt.savefig(output_file)

plt.show()

print(f"Графік збережено у файлі: {output_file}")
