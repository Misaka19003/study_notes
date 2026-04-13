
from qiskit.primitives import StatevectorSampler#导入Qiskit新版标准运行器StatevectorSampler

from 构建贝尔态_核心代码 import qc

sampler = StatevectorSampler()#创建一个模拟采样器
result = sampler.run([qc], shots=1024).result()#运行量子电路 1024 次
print(result[0].data.meas.get_counts())#打印测量结果的统计次数