import matplotlib.pyplot as plt

labels = '1', '0', 'Deactivated'
colors = ['Red', 'Green', 'Grey']
sizes = [1/3, 1/3, 1/3]
explode = ( 0, 0, 0)  # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()