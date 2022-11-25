# penicillin-prediction
Test repository for exploring Penicillin production prediction

# Ref Paper
https://www.sciencedirect.com/science/article/pii/S0098135418305106#tbl0001


## Todos
- Send Dataset/Inputs+Outputs & Expected Results
- DNN -> 1v-Regr (explore+ more)

<!--
Penicillin is produced by the fungus Penicillium chrysogenum which requires lactose, other sugars, and a source of nitrogen (in this case a yeast extract) in the medium to grow well. -->

Accuracy
|                | Deep NN | Regression |
|----------------|---------|------------|
| **Tollerance** |         |            |
| 10%            | 63%     | 60%         |
| 1%             | 7%      | 6.8%        |
| *0.1%          | 0.7%    | 0%        |
\*: Target rtol

<style>
    tr:nth-child(2) td:nth-child(2){
        background: #2f2;
        color: #fff;
    }
    tr:nth-child(3) td:nth-child(2){
        background: #ff4;
        color: #000;
    }
    tr:nth-child(4) td:nth-child(2){
        background: #f44;
        color: #fff;
    }
</style>