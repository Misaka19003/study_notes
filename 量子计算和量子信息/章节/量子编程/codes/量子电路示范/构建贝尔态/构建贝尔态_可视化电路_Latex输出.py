from qiskit import QuantumCircuit
import matplotlib.pyplot as plt#导入绘图模块

from 构建贝尔态_核心代码 import qc

with open('circuit.tex', 'w') as f:
    f.write(qc.draw(output='latex_source'))#生成 LaTeX 文件