import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 微軟正黑體

# Data
cohorts = ['第二屆', '第三屆', '第四屆']
active_members = [4, 4, 7]
total_members = [4, 7, 16]

# Bar width and positions
bar_width = 0.35
index = np.arange(len(cohorts))

# Create the plot
fig, ax = plt.subplots()
bars1 = ax.bar(index, active_members, bar_width, label='活躍成員')
bars2 = ax.bar(index + bar_width, total_members, bar_width, label='全部成員')

# Labels and titles
ax.set_xlabel('屆別')
ax.set_ylabel('成員數量')
ax.set_title('iTron 歷屆成員數量比較')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(cohorts)
ax.legend()

# Display the chart
plt.tight_layout()
plt.savefig("itron-members.png", dpi=300)