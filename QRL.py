# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute 
from qiskit.tools.visualization import circuit_drawer
import random
from qiskit import available_backends, execute, register, get_backend
from qiskit.tools.qi.qi import state_fidelity
from qiskit import Aer

# Create a Quantum Register with 3 qubits.
q = QuantumRegister(3, 'q')
c = ClassicalRegister(1, 'c')

# Create a Quantum Circuit acting on the q register
qc = QuantumCircuit(q, c)

a = random.uniform(0, 3.1415/2)
b = random.uniform(0, 3.1415/2)
qc.u2(a, b, q[2])
qc.cx(q[1], q[2])