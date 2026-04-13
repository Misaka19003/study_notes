from qiskit import QuantumCircuit
import matplotlib.pyplot as plt#导入绘图模块

from 构建贝尔态_核心代码 import qc

fig = qc.draw(output='mpl')#绘制但不立即显示
plt.show()#弹出窗口