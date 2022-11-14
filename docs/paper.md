# Simulator & Dataset Summary

## Model Outputs
![Hidden Layers](/assets/model.jpg)

### Simulator Design
```mermaid
flowchart LR

Legend1("F(x) = Flow Rate of X")

Sim[Simulator]

AutoInputs[("
F<sub>a/b</sub> = F(Acid/Base)
F<sub>c</sub> = F(Cooling Water)")]
ManInputs[("
F<sub>s</sub> = F(Substrate)
F<sub>w</sub> = F(Water)
F<sub>g</sub> = AerationRate
F<sub>PAA</sub> = F(Phenylacetic Acid)
F<sub>g</sub> = F(Aeration Rate)
F<sub>N</sub> = F(Nitrogen)
F<sub>dis</sub> = F(discharge)
RPM = AgitatorRate")]

SensorOutputs[("
T = Temperature
pH = log conc of H
DO<sub>2</sub> = Dissolved Oxygen
W = Weight
P<sub>ag</sub> = Agitator Power
CO<sub>2,og</sub> = CO2 off gas
O<sub>2,og</sub> = O2 off gas
")]
PhysOutputs[("
P = Penicillin
PAA = PhenylAcetic Acid
N = Nitrogen
µ<sub>vis</sub> = Viscosity
")]
PATOutputs[("
Spec = Raman Spectroscopy
")]




AutoInputs & ManInputs --> Sim --> SensorOutputs & PhysOutputs & PATOutputs
```

### Control Strategy for Variables

<table>
   <thead>
      <tr class="rowsep-1">
         <th scope="col">Variable reference</th>
         <th scope="col">Primary control variables</th>
         <th scope="col">Control strategy</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>Dissolved O2 (<em>DO<sub>2</sub> -</em> mg L<sup>−1</sup>)</td>
         <td>F<sub>g</sub>,RPM</td>
         <td>&gt;10% of saturation</td>
      </tr>
      <tr>
         <td>Weight (<em>W -</em> kg)</td>
         <td>F<sub>water</sub>,F<sub>s</sub>,F<sub>a/b</sub>,F<sub>PAA,</sub>F<sub>dis</sub></td>
         <td>Maintain between 7 ×10<sup>4</sup> and 11×10<sup>4</sup> kg</td>
      </tr>
      <tr>
         <td>pH (<em>pH</em>)</td>
         <td>F<sub>a/b</sub></td>
         <td>PID control algorithm</td>
      </tr>
      <tr>
         <td>Temperature (<em>T - K</em>)</td>
         <td>F<sub>c</sub></td>
         <td>PID control algorithm</td>
      </tr>
      <tr>
         <td>Off-gas values (CO<sub>2,og</sub> &amp; O<sub>2, og</sub> -%)</td>
         <td>F<sub>g,</sub> RPM</td>
         <td>Not controlled</td>
      </tr>
      <tr>
         <td>Penicillin (<em>P -</em> g L<sup>−1</sup>)</td>
         <td>F<sub>S</sub>,F<sub>oil</sub>,F<sub>PAA</sub>,F<sub>N</sub></td>
         <td>Maximise production</td>
      </tr>
      <tr>
         <td>Biomass (<em>X -</em> g L<sup>−1</sup>)</td>
         <td>F<sub>S</sub>,F<sub>oil</sub>,F<sub>PAA</sub>,F<sub>N</sub></td>
         <td>Maximise production</td>
      </tr>
      <tr>
         <td>Phenylacetic acid (<em>PAA</em> - mg L<em><sup>−1</sup></em>)</td>
         <td>F<sub>PAA</sub></td>
         <td>Maintain between 600 and 1800 mg L<sup>−1</sup></td>
      </tr>
      <tr>
         <td>Nitrogen (<em>N -</em> mg L<sup>−1</sup>)</td>
         <td>N<sub>shots,</sub>F<sub>oil</sub>,F<sub>PAA</sub></td>
         <td>Maintain above 300 mg L<sup>−1</sup></td>
      </tr>
      <tr>
         <td>Viscosity (<em>μ</em> - cP)</td>
         <td>F<sub>water</sub></td>
         <td>Maintain below 100 cP</td>
      </tr>
      <tr>
         <td>Substrate (<em>S -</em> g L<sup>−1</sup>)</td>
         <td>F<sub>s</sub>,F<sub>oil</sub></td>
         <td>Maintain between 5 × 10<sup>−3</sup> and 1  ×  10<sup>−3</sup> g L<sup>−1</sup></td>
      </tr>
   </tbody>
</table>

## Data Cleanup
In the `data_cleanup.ipynb` we take our data set and drop all columns with the following critera (with reasons)
- *Raman Spectral Data 0-2400* (2402 columns): 11 Inputs cannot predit 2400 outputs
- *More than 60% Empty* (7 columns): Columns which are more than 60% empty contribute no value
- *More than 85% 0s* (0 columns): Columns which are mostly 0 do not add value and are fillers

The following variables are also dropped
- Ammonia: No use to us
- PAT: No use to us, is for machine ref
- Batch ID: No use to us, is for machine ref
- Agitator RPM: All values are 100 constant
- Fault Flag: We have access to fault reference so flag is not needed