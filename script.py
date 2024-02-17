import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Parse the XML file
tree = ET.parse("Results.xml")
root = tree.getroot()

# Initialize lists to store data
class_names = []
metrics = {
    "WMC": [],
    "DIT": [],
    "NOC": [],
    "CBO": [],
    "RFC": [],
    "LCOM": [],
    "LCOM3": [],
}

# Extract data from XML and append to lists
for class_element in root.findall("class"):
    class_name = class_element.find("name").text.split(".")[-1]
    class_names.append(class_name)
    for metric in metrics:
        metric_value = float(class_element.find(metric.lower()).text)
        metrics[metric].append(metric_value)

# Plotting
plt.figure(figsize=(12, 8))

bar_width = 0.15
num_classes = len(class_names)
index = range(num_classes)

for i, metric in enumerate(metrics):
    plt.bar(index, metrics[metric], bar_width, label=metric)

    # Move to the next group of bars
    index = [x + bar_width for x in index]

plt.xlabel("Class Names")
plt.ylabel("Metrics")
plt.title("SRE Metrics Analysis")
# Set the x-axis ticks to align with NOC metric
plt.xticks(ticks=range(len(class_names)), labels=class_names, rotation=45, ha="right")

plt.legend()
plt.grid(True)
plt.tight_layout(w_pad=5.0, h_pad=1.0)

plt.show()
