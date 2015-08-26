var sysTable=document.getElementById("sysTable");

var dis_T=sysTable.rows[1].cells[1];
var CostProd,priceUS,priceEU,r,N;
N=5;
var Profit=new Array(N);

var ExCNYtoUS=new Array(N);
var ExEUROtoUS=new Array(N);

var USProd=new Array(N);
var EUProd=new Array(N);

var DCUSInv=new Array(N);
var DCEUInv=new Array(N);

var TPDCUS=new Array(N);
var TPDCEU=new Array(N);

var USInv=new Array(N);
var EUInv=new Array(N);

var DemandUS=new Array(N);
var SalesUS=new Array(N);
var DemandEU=new Array(N);
var SalesEU=new Array(N);

var dis_ExCNYtoUS=ExTable.rows[2].cells[1];
var dis_ExEUROtoUS=ExTable.rows[3].cells[1];
var dis_DCUSInv=document.getElementById("dis_inventoryDC_US");
var dis_DCEUInv=document.getElementById("dis_inventoryDC_EU");
var dis_tpDCUS=document.getElementById("dis_transDC2US");
var dis_tpDCEU=document.getElementById("dis_transDC2EU");
var dis_totalProfit=document.getElementById("totalprofit_chain2");

var dis_DemandUS=document.getElementById("dis_demandUS");
var dis_SalesUS=document.getElementById("dis_saleUS");
var dis_DemandEU=document.getElementById("dis_demandEU");
var dis_SalesEU=document.getElementById("dis_saleEU");

var dis_CostProd=sysTable.rows[7].cells[1];
var dis_priceUS=sysTable.rows[4].cells[1];
var dis_priceEU=sysTable.rows[5].cells[1];
var dis_r=sysTable.rows[6].cells[1];

var input_USProd=document.getElementById("input_prodUSPlant");
var input_EUProd=document.getElementById("input_prodEUPlant");

function stepRun(){
    var t=dis_T.innerHTML;

    if(t>=1&&t<=N){
        switch (t){
            case '1':{
                alert('sss');
                DCUSInv[t-1]=0;
                DCEUInv[t-1]=0;
                TPDCUS[t-1]=0;
                TPDCEU[t-1]=0;
                USInv[t-1]=0;
                EUInv[t-1]=0;
                SalesUS[t-1]=0;
                SalesEU[t-1]=0;

                USProd[t-1]=eval(input_USProd).value;
                EUProd[t-1]=eval(input_EUProd).value;

                dis_DCUSInv.innerHTML=DCUSInv[t-1];
                dis_DCEUInv.innerHTML=DCEUInv[t-1];
                dis_tpDCUS.innerHTML=TPDCUS[t-1];
                dis_tpDCEU.innerHTML=TPDCEU[t-1];
                dis_USInv.innerHTML=USInv[t-1];
                dis_EUInv.innerHTML=EUInv[t-1];
                dis_SalesUS.innerHTML=SalesUS[t-1];
                dis_SalesEU.innerHTML=SalesEU[t-1];

                Profit[t-1]=0;
                break;
            }
            case '2':{
                DCUSInv[t-1]=USProd[t-2];
                DCEUInv[t-1]=EUProd[t-2];
                TPDCUS[t-1]=0;
                TPDCEU[t-1]=0;
                USInv[t-1]=0;
                EUInv[t-1]=0;
                SalesUS[t-1]=0;
                SalesEU[t-1]=0;

                USProd[t-1]=eval(input_USProd).value;
                EUProd[t-1]=eval(input_EUProd).value;

                dis_DCUSInv.innerHTML=DCUSInv[t-1];
                dis_DCEUInv.innerHTML=DCEUInv[t-1];
                dis_tpDCUS.innerHTML=TPDCUS[t-1];
                dis_tpDCEU.innerHTML=TPDCEU[t-1];
                dis_USInv.innerHTML=USInv[t-1];
                dis_EUInv.innerHTML=EUInv[t-1];
                dis_SalesUS.innerHTML=SalesUS[t-1];
                dis_SalesEU.innerHTML=SalesEU[t-1];

                Profit[t-1]=(1+r)*Profit[t-2]+priceUS*SalesUS[t-1]+ExEUROtoUS[t-1]*priceEU*SalesEU[t-1]-ExCNYtoUS[t-1]*CostProd*(USProd[t-1]+EUProd[t-1]);
                break;
            }
            case '3':{
                DCUSInv[t-1]=USProd[t-2];
                DCEUInv[t-1]=EUProd[t-2];
                TPDCUS[t-1]=DCUSInv[t-2];
                TPDCEU[t-1]=DCEUInv[t-2];
                USInv[t-1]=0;
                EUInv[t-1]=0;
                SalesUS[t-1]=0;
                SalesEU[t-1]=0;

                USProd[t-1]=eval(input_USProd).value;
                EUProd[t-1]=eval(input_EUProd).value;

                dis_DCUSInv.innerHTML=DCUSInv[t-1];
                dis_DCEUInv.innerHTML=DCEUInv[t-1];
                dis_tpDCUS.innerHTML=TPDCUS[t-1];
                dis_tpDCEU.innerHTML=TPDCEU[t-1];
                dis_USInv.innerHTML=USInv[t-1];
                dis_EUInv.innerHTML=EUInv[t-1];
                dis_SalesUS.innerHTML=SalesUS[t-1];
                dis_SalesEU.innerHTML=SalesEU[t-1];

                Profit[t-1]=(1+r)*Profit[t-2]+priceUS*SalesUS[t-1]+ExEUROtoUS[t-1]*priceEU*SalesEU[t-1]-ExCNYtoUS[t-1]*CostProd*(USProd[t-1]+EUProd[t-1]);
                break;
            }
            default :{
                DCUSInv[t-1]=USProd[t-2];
                DCEUInv[t-1]=EUProd[t-2];
                TPDCUS[t-1]=DCUSInv[t-2];
                TPDCEU[t-1]=DCEUInv[t-2];
                USInv[t-1]=DCUSInv[t-2]+TPDCUS[t-2]-SalesUS[t-2];
                EUInv[t-1]=DCEUInv[t-2]+TPDCEU[t-2]-SalesEU[t-2];
                SalesUS[t-1]=Math.min(DemandUS[t-1],DCUSInv[t-1]);
                SalesEU[t-1]=Math.min(DemandEU[t-1],DCEUInv[t-1]);

                USProd[t-1]=eval(input_USProd).value;
                EUProd[t-1]=eval(input_EUProd).value;

                dis_DCUSInv.innerHTML=DCUSInv[t-1];
                dis_DCEUInv.innerHTML=DCEUInv[t-1];
                dis_tpDCUS.innerHTML=TPDCUS[t-1];
                dis_tpDCEU.innerHTML=TPDCEU[t-1];
                dis_USInv.innerHTML=USInv[t-1];
                dis_EUInv.innerHTML=EUInv[t-1];
                dis_SalesUS.innerHTML=SalesUS[t-1];
                dis_SalesEU.innerHTML=SalesEU[t-1];

                Profit[t-1]=(1+r)*Profit[t-2]+priceUS*SalesUS[t-1]+ExEUROtoUS[t-1]*priceEU*SalesEU[t-1]-ExCNYtoUS[t-1]*CostProd*(USProd[t-1]+EUProd[t-1]);
            }

        }

        dis_totalProfit.innerHTML=Profit[t-1];

        if(t<N){

            dis_T.innerHTML++;
        }
    }

}