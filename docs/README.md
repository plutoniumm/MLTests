# penicillin-prediction
Repository for exploring Penicillin production prediction application


## Folder Structure

```
root
└─── README.md
│
└───pdf
└───docs
└───server
└───client
└───ml
```

## Main Objective Variables
We need to use the following inputs
1. Time (h)
2. Substrate concentration(S:g/L)
3. Sugar feed rate(Fs:L/h)
4. Acid flow rate(Fa:L/h)
5. Base flow rate(Fb:L/h)
6. Ammonia
7. Temperature(T:K)
8. Water Flow [SUM OF (Fc+Fh+Fw)]

In order to accurately predict
1. Penicillin concentration(P:g/L)
2. pH(pH:pH)
3. Vessel Volume(V:L)


## Timeline
```mermaid
gantt
    title Expected November
    dateFormat  DD-MM
    axisFormat  %d %b

    %% Start :milestone, m1, 07-11, 2min

    Test NN !PCA :active, a1, 10-11, 8d
    Initial Docs :active, b1, 11-11, 5d
    Test NN + PCA:a2, after b1, 6d

    Test REGR:a3, after a2, 4d
```

```mermaid
gantt
    title Expected December
    dateFormat  DD-MM
    axisFormat  %d %b

    Unplanned:a1, 01-12, 24d
```


## Overview

- **PCA**: Principle Component Analysis
- **NN**: Neural Net


```mermaid
flowchart LR
   I[(Data)] --> PCA --> NN --> O[(Output)]

   NN <-.-> Model

   Input --> Model --> OEO[Output] --> Correction
   EO[Expected Output] --> OEO
```
