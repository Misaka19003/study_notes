from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])#创建一个简单的贝尔态电路

print(qc)#直接在控制台打印电路