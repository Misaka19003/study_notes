from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])#创建一个简单的贝尔态电路

with open('circuit.tex', 'w') as f:
    f.write(qc.draw(output='latex_source'))#生成 LaTeX 文件