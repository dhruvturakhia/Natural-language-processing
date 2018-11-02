//model File
//parameters

int n = ...; //number of cargos
int m = ...; //number of compartments

range cargos = 1...n;
range comps = 1...m;



float profit[cargos] =...;
float weight[cargos] =...;
float volume[cargos] =...;


float weight_cap[comps] =...;
float space_cap[comps] =...;



//variables

dvar float+ x[cargos][comps];
dvar float+ y;

maximize sum(i in cargos, j in comps) profit[i]*x[i][j];


subject to {
  forall (i in cargos)
    available_weight:
      sum(j in comps) x[i][j] <= weight[i];

  forall (j in comps)
    weight_capacity:
      sum(i in cargos) x[i][j] <= weight_cap[i];

    forall (j in comps)
      space_capacity:
        sum(i in cargos) volume[i][j] <= space_cap[i];


      forall (j in comps)
        balance_plane:
          sum(i in cargos) x[i][j]/weight_cap[j] == y;
}


//data File
//move excle file in the project

n = 4;
m = 3;


SheetConnection my_Sheet("day 1 - excel.xlsx")

profit from SheetRead(my_sheet, "profit");
weight from SheetRead(my_sheet, "weight");
volume from SheetRead(my_sheet, "volume");


weight_cap from SheetRead(my_sheet, "weight_cap");
space_cap from SheetRead(my_sheet, "spcae_cap");
