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

delta = 2*pi/3
eta = 1.2
aa = random.uniform(-delta/2, delta/2)
bb = random.uniform(-delta/2, delta/2)
a = array.array('d',[aa])
b = array.array('d',[bb])

ex = 3.130756514997222
ey = 3.9944049908247625
ez = 2.6848785549652145

env = [
       cos(ex/2)*complex(1,0),
       sin(ex/2)*complex(cos(ey), sin(ey))
       ]
env

'''
print (str(ex))
print (str(ey))
print (str(ez))
'''

#Fidelty 
fidelity = 0
#old fidelity
ofidelity = 0


def updDelta (num, delta):
   if(num == 1):
       delta = delta/eta
   else:
       delta = delta*eta
   return 0;

cycle  = 39
'''
q = QuantumRegister(1, 'q')
c = ClassicalRegister(1)
qc = QuantumCircuit(q,c)

qc.u3(ex, ey, ez, q[0])

qc.measure(q[0], c[0])

job = execute(qc, backend=backend, shots=shots, max_credits=max_credits)
result = job.result()
outcome = int(str(result.get_counts(qc))[2])
'''

#state_fidelity(env, [q[2]])


for i in range(1, cycle+1):
    print("\nIteration Number = " + str(i))
    backend = IBMQ.get_backend('ibmq_qasm_simulator')
    #Creating Gates
    #q0 is |A>
    #q1 is |R>
    #q2 is |E>
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(1, 'c')
    qc = QuantumCircuit(q,c)
    #qc.initialize(env, [q[2]])
    
    #Initializing Environment
    qc.u3(ex, ey, ez, q[2])
    #qc.initialize(env, [q[2]])
    
#    state_fidelity(env, q[2])
    for j in range(1, i):
        qc.rz(-b[j],q[2])
        for k in range(1, j):
            qc.rx(a[j],q[0])
            qc.rz(b[j],q[0])
        qc.rx(a[j],q[0])
        qc.rz(b[j],q[0])
        for k in range(1, j):
            qc.rz(-b[j],q[0])
            qc.rx(-a[j],q[0])
        qc.rx(-a[j],q[2])
    
     #Copying env to registe
    qc.cx(q[2],q[1])    
    qc.measure(q[1], c[0])



#qc.cx(q[1], q[4])

#backend_sim = Aer.get_backend('qasm_simulator')
#result = execute(qc, backend_sim).result()
#print(result.get_counts(qc))
#i = 1
#for i in range(1,3):

    job = execute(qc, backend=backend, shots=shots, max_credits=max_credits)
    result = job.result()
    outcome = int(str(result.get_counts(qc))[2])
    #qc_state = result.get_statevector(qc)
    #print(qc_state)
    #state_fidelity(env, qc_state)
    print('Result = ' + str(result.get_counts(qc)))
    print ('Outcome = ' + str(outcome))
    aa = random.uniform(-delta/2, delta/2)
    print ('aa = ' + str(aa))
    bb = random.uniform(-delta/2, delta/2)
    print ('bb = ' + str(bb))
    if(outcome == 1):
        delta = delta*eta
        a.append(aa)
        b.append(bb)
    else:
        delta = delta/eta
        a.append(0)
        b.append(0)
    #circuit_drawer(qc)
    
    q = QuantumRegister(1, 'q')
    qc2 = QuantumCircuit(q)
    
    qc2.rz(0, q[0])
    
    for j in range(1, i+1):
        for k in range(1, j):
            qc2.rz(-b[j],q[0])
            qc2.rx(-a[j],q[0])
        qc2.rx(a[j],q[0])
        qc2.rz(b[j],q[0])
        for k in range(1, j):
            qc2.rx(a[j],q[0])
            qc2.rz(b[j],q[0])

    backend = Aer.get_backend('statevector_simulator')
    job = execute(qc2, backend)
    qc2_state = job.result().get_statevector(qc2)
    qc2_state
    fidelity = state_fidelity(env, qc2_state)
    print('Fidelity = ' + str(state_fidelity(env, qc2_state)))
    #if((fidelity>=0.9)&(ofidelity <= 0.9)):
    #    delta = pi/8
    #print('Delta = ' + str(delta))
    ofidelity = fidelity
    #circuit_drawer(qc2)
    
q = QuantumRegister(1, 'q')
qc = QuantumCircuit(q)

for j in range(1, cycle+1):
    for k in range(1, j):
        qc.rz(-b[j],q[0])
        qc.rx(-a[j],q[0])
    qc.rx(a[j],q[0])
    qc.rz(b[j],q[0])
    for k in range(1, j):
        qc.rx(a[j],q[0])
        qc.rz(b[j],q[0])

backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
qc_state = job.result().get_statevector(qc)
qc_state
print('Final Fidelity = ' + str(state_fidelity(env, qc_state)))
#circuit_drawer(qc)

    
#counts_exp = result_exp.get_counts(qc)
#print(counts_exp)
#plot_histogram(counts_exp)

#circuit_drawer(qc)