from qiskit import QuantumCircuit#从Qiskit库里导入量子电路工具QuantumCircuit
from qiskit.primitives import StatevectorSampler#导入Qiskit新版标准运行器StatevectorSampler

qc = QuantumCircuit(2)#创建一个 2 个量子比特的电路
qc.h(0)#给第0号量子比特加H门
qc.cx(0, 1)#加受控非门 CX
qc.measure_all()#测量所有量子比特

sampler = StatevectorSampler()#创建一个模拟采样器
result = sampler.run([qc], shots=1024).result()#运行量子电路 1024 次
print(result[0].data.meas.get_counts())#打印测量结果的统计次数