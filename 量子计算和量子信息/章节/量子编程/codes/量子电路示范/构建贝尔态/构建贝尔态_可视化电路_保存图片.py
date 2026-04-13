from qiskit import QuantumCircuit
import matplotlib.pyplot as plt#导入绘图模块

from 构建贝尔态_核心代码 import qc

qc.draw(output='mpl', filename='circuit.png')#绘制并保存为文件