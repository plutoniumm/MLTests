# penicillin-prediction
Test repository for exploring Penicillin production prediction, may not work


# Bioreactor
Requirements of a BioReactor Digital Twin
- Reactor Body: Can be made in any 3D sim software
- Sensor Suite: Basic NN can do all inferences as predictions
- Reaction Simulator: No Technology exists.

## Reactor Body
Easiest to make and can be done in a few steps in any 3D sim software with 2-3 people within a week. In our case even Blender and NVIDIA Omniverse

## Sensor Suite
Minimal Effort. There will be n inputs which will give output of production of penecillin. We are currently in the process of making a small repository which contains 2 pieces of code which will tentaively do the following
1. Take inputs of environment variables and predict quality of output: ASSUMING PERFECT REACTION. This will employ a simple DNN with 2 hidden layers
2. In case of poor quality output suggest changes to input to improve quality of product. This will most likely be a simple algebra problem with statement 1 as a blackbox dependency

## Reaction Simulator
The closest we have come to actual reaction simulation is
- Quantum Computers: 100 qubits max, can simulate a few electrons atom at best that to noisily. And is 10 years away from even smallest compounds as per Google Quantum AI Team, IBM Quantum & Qiskit team and Xanadu AI & Pennylane team the 3 leading quantum producers. [Google Quantum Symposium (video is unlisted)](https://www.youtube.com/watch?v=__wLbTRZCQA)
- ANSYS Chemkin Pro: Ansys chemikin pro, does not simulate a reaction. It simulates the flow of reactants & ASSUMES IDEAL REACTION CONDITIONS. So in bioreactor if we use this it basically assumes everything is going well in reactions, defeating whole purpose [Website states they assume ideal rxn](https://www.ansys.com/products/fluids/ansys-chemkin-pro)
- Quantum Espresso Fortran Simulator: Industry leading software for chemical reactions. Is very slow so requires server farms and months to be able to simulate any molecule of moderately decent size for a few seconds. Is completely impractical for realtime use case we need

# Conclusion
In the short term it seems that a bioreactor digital twin is impossible to create without vast resources and therefore impractical to create a full digital twin

The alternative could be that if the client company is able to provide an API which does the reaction simulation for us in realtime then it can be plugged in to the specific type of reactor and done. This however defeats the purpose since the difficult part is not making the digital twin but the reaction simulator itself