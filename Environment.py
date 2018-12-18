#This code tries to clone a qubit state, called the Environment here, into another qubit called the Agent
import numpy
import math
from math import pi, cos, sin
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, IBMQ, Aer, available_backends, execute, register, get_backend
from qiskit.tools.visualization import circuit_drawer
from qiskit.tools.qi.qi import state_fidelity
import random 
import array
#import Qconfig_IBMQ_network
#import Qconfig_IBMQ_experience

api_token='55bc88103549da44c2e47840f4f2768d286c5fa8975960c49b202c55a802117bbf970051e687ddf1d7403ca25dc46947d6fa844881841e41a6d5d31d33998c04'

#from IBMQuantumExperience import IBMQuantumExperience
#IBMQ.load_accounts()
#IBMQ.stored_accounts()
IBMQ.enable_account(api_token)
IBMQ.load_accounts()
#print("Available backends:")
#IBMQ.backends()
#IBMQ.get_backend()
backend = IBMQ.get_backend('ibmq_qasm_simulator')
#backend = Aer.get_backend('statevector_simulator')
#print(backend)

       
shots = 1         # Number of shots to run the program (experiment); maximum is 8192 shots.
max_credits = 3        # Maximum number of credits to spend on executions. 


ex = random.uniform(4*pi/7, pi)
ey = random.uniform(4*pi/7, 2*pi)
ez = random.uniform(4*pi/7, 2*pi)

print (str(ex))
print (str(ey))
print (str(ez))
env = [
       cos(ex/2)*complex(1,0),
       sin(ex/2)*complex(cos(ey), sin(ey))
       ]
env

q = QuantumRegister(1, 'q')
qc = QuantumCircuit(q)

qc.rz(0,q[0])
#qc.u3(ex, ey, ez, q[0])

backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend, shots=6000)
qc_state = job.result().get_statevector(qc)
qc_state
print(state_fidelity(env, qc_state))
circuit_drawer(qc)