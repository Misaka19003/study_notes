from qiskit import QuantumCircuit#从 Qiskit 库中导入 QuantumCircuit 类

qc = QuantumCircuit(2)#创建一个拥有2个量子比特的电路
qc.h(0)#对第0号量子比特施加H门
qc.cx(0, 1)#以第0号量子比特为控制位，第1号量子比特为目标位做一个CNOT门（受控非门）
qc.measure_all()#测量所有量子比特