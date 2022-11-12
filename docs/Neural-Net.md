# Neural Net Arch

## Model Choice
Since not much complexity is needed due to `Array<int>` inputs and `Array<int>` outputs it makes most sense to go for a simple Input Layer and Output layer with 2 hidden layers network

The 2 hidden layers are also Overkill and are included for future-proofing

Hidden Layer Size formula
$$
N_h = \frac{N_s}{\alpha ∗ ( N_i + N_o)}
$$