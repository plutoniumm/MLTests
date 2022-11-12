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


## Timeline
```mermaid
gantt
    title Expected November
    dateFormat  DD-MM
    axisFormat  %d %b

    %% Start :milestone, m1, 07-11, 2min

    Test NN !PCA :active, a1, 10-11, 8d
    Initial Docs :active, b1, 11-11, 5d
    Leave: l1, 18-11, 4d
    Test NN + PCA:a2, after l1, 4d

    Adjusted NN 4 proj:a3, after a2, 3d
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
