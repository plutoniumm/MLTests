# penicillin-prediction
Test repository for exploring Penicillin production prediction, may not work


# Bioreactor
Requirements of a BioReactor Digital Twin
- Reactor Body: Can be made in any 3D sim software
- Sensor Suite: Basic NN can do all inferences as predictions
- Reaction Simulator: No Technology exists.

# Reactor Body
Easiest to make and can be done in a few steps in any 3D sim software with 2-3 people within a week. In our case even Blender and NVIDIA Omniverse

# Sensor Suite
Minimal Effort. There will be n inputs which will give output of production of penecillin.

The closest we have come to actual reaction simulation is
- Quantum Computers: 100 qubits max, can simulate 1 atom at best. And is 10 years away from even smallest compounds as per Google Quantum AI Team, IBM Quantum & Qiskit team and XANADU AI & Pennylane team the 3 leading quantum producers
- ANSYS Chemkin Pro: Ansys chemikin pro, does not simulate a reaction. It simulates the flow of reactants & ASSUMES IDEAL REACTION CONDITIONS. So in bioreactor if we use this it basically assumes everything is going well in reactions, defeating whole purpose
- Quantum Espresso Fortran Simulator: Industry leading software for chemical reactions.