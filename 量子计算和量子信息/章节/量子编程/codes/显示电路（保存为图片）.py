from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])#创建一个简单的贝尔态电路

qc.draw(output='mpl', filename='circuit.png')#绘制并保存为文件