"""Sprint burndown chart. Run: python burndown.py  (pip install matplotlib)"""
import matplotlib.pyplot as plt

total_points = 40
days = list(range(0, 11))
completed = [0, 3, 5, 9, 12, 18, 22, 27, 31, 36, 40]
ideal = [total_points - total_points * d / 10 for d in days]
actual = [total_points - c for c in completed]

plt.plot(days, ideal, "--", label="Ideal")
plt.plot(days, actual, marker="o", label="Actual")
plt.xlabel("Sprint day"); plt.ylabel("Story points remaining")
plt.title("Sprint Burndown"); plt.legend(); plt.grid(alpha=.3)
plt.savefig("burndown.png", dpi=150)
