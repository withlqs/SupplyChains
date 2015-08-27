var sysTable=document.getElementById("sysTable");
var ExTable=document.getElementById("ExTable");

var dis_T = sysTable.rows[5].cells[1];

var CostProd,priceUS,priceEU,r,CostTranship,N;
N=5;
var Profit=new Array(N);
var ExCNYtoUS=new Array(N);
var ExEUROtoUS=new Array(N);

var DCInventory=new Array(N);
var Prod=new Array(N);

var DCUS=new Array(N);
var DCEU=new Array(N);

var USEU=new Array(N);
var EUUS=new Array(N);

var TPDCUS=new Array(N);
var TPDCEU=new Array(N);

var TPUSEU=new Array(N);
var TPEUUS=new Array(N);

var USInv=new Array(N);
var EUInv=new Array(N);

var DemandUS=new Array(N);
var SalesUS=new Array(N);
var DemandEU=new Array(N);
var SalesEU=new Array(N);

var dis_ExCNYtoUS=ExTable.rows[1].cells[1];
var dis_ExEUROtoUS=ExTable.rows[2].cells[1];
var dis_DCInv=document.getElementById("dis_inventoryDC");

var dis_USInv=document.getElementById("dis_inventoryUS");
var dis_EUInv=document.getElementById("dis_inventoryEU");

var dis_DemandUS=document.getElementById("dis_demandUS");
var dis_SalesUS=document.getElementById("dis_saleUS");
var dis_DemandEU=document.getElementById("dis_demandEU");
var dis_SalesEU=document.getElementById("dis_saleEU");
var dis_totalProfit=document.getElementById("totalprofit_chain1");

var dis_CostProd=sysTable.rows[1].cells[1];
var dis_priceUS=sysTable.rows[2].cells[1];
var dis_priceEU=sysTable.rows[3].cells[1];
var dis_r=sysTable.rows[4].cells[1];
var dis_CostTranship=sysTable.rows[6].cells[1];

var input_Prod=document.getElementById("input_prodPlant");
var input_transDC2US=document.getElementById("input_transDC2US");
var input_transDC2EU=document.getElementById("input_transDC2EU");
var input_transUS2EU=document.getElementById("input_transUS2EU");
var input_transEU2US=document.getElementById("input_transEU2US");


function stepRun(){


//    var t=dis_T.innerHTML;
//
//    if(t>=1&&t<=N) {
//        <!--Display EX Rate-->
//
//        <!---->
//        switch (t){
//            case '1':{
//                <!--t=1,Inital 0-->
//                alert("T=1");
//                DCInventory[0] = 0;
//                TPDCUS[0] = 0;
//                TPDCEU[0] = 0;
//                TPUSEU[0] = 0;
//                TPEUUS[0] = 0;
//                USInv[0] = 0;
//                EUInv[0] = 0;
//                SalesUS[0] = 0;
//                SalesEU[0] = 0;
//
//                Prod[t - 1] = eval(input_Prod).value;
//                DCUS[t - 1] = eval(input_transDC2US).value;
//                DCEU[t - 1] = eval(input_transDC2EU).value;
//                USEU[t - 1] = eval(input_transUS2EU).value;
//                EUUS[t - 1] = eval(input_transEU2US).value;
//
//                dis_DCInv.innerHTML = DCInventory[0];
//                dis_tpDCUS.innerHTML = TPDCUS[0];
//                dis_tpDCEU.innerHTML = TPDCEU[0];
//                dis_tpUSEU.innerHTML = TPUSEU[0];
//                dis_tpEUUS.innerHTML = TPEUUS[0];
//                dis_USInv.innerHTML = USInv[0];
//                dis_EUInv.innerHTML = EUInv[0];
//                dis_SalesUS.innerHTML = SalesUS[0];
//                dis_SalesEU.innerHTML = SalesEU[0];
//                dis_DemandUS.innerHTML = DemandUS[t - 1];
//                dis_DemandEU.innerHTML = DemandEU[t - 1];
//
//
//                alert(Prod[t-1]+","+dis_DCInv.innerHTML+","+DCInventory[t-1]);
//                Profit[0] = 0;
//                break;
//            }
//            case '2':{
//                alert("T=2");
//                DCInventory[t - 1] = DCInventory[t - 2] + Prod[t - 2] - DCUS[t - 2] - DCEU[t - 2];
//                TPDCUS[t - 1] = DCUS[t - 2];
//                TPDCEU[t - 1] = DCEU[t - 2];
//                TPUSEU[t - 1] = USEU[t - 2];
//                TPEUUS[t - 1] = EUUS[t - 2];
//
//                USInv[t - 1] = 0;
//                EUInv[t - 1] = 0;
//                SalesUS[t - 1] = 0;
//                SalesEU[t - 1] = 0;
//
//                Prod[t - 1] = eval(input_Prod).value;
//                DCUS[t - 1] = eval(input_transDC2US).value;
//                DCEU[t - 1] = eval(input_transDC2EU).value;
//                USEU[t - 1] = eval(input_transUS2EU).value;
//                EUUS[t - 1] = eval(input_transEU2US).value;
//
//                dis_DCInv.innerHTML = DCInventory[t - 1];
//                dis_tpDCUS.innerHTML = TPDCUS[t - 1];
//                dis_tpDCEU.innerHTML = TPDCEU[t - 1];
//                dis_tpUSEU.innerHTML = TPUSEU[t - 1];
//                dis_tpEUUS.innerHTML = TPEUUS[t - 1];
//                dis_USInv.innerHTML = USInv[t - 1];
//                dis_EUInv.innerHTML = EUInv[t - 1];
//                dis_SalesUS.innerHTML = SalesUS[0];
//                dis_SalesEU.innerHTML = SalesEU[0];
//                dis_DemandUS.innerHTML = DemandUS[t - 1];
//                dis_DemandEU.innerHTML = DemandEU[t - 1];
//
//
//
//                Profit[t - 1] = (1 + r) * Profit[t - 2] + priceUS * SalesUS[t - 1] + ExEUROtoUS[t - 1] * priceEU * SalesEU[t - 1] - ExCNYtoUS[t - 1] * CostProd * Prod[t - 1] - CostTranship * (USEU[t - 1] + EUUS[t - 1]);
//                break;
//            }
//            default :{
//                alert("T=Other");
//                DCInventory[t - 1] = DCInventory[t - 2] + Prod[t - 2] - DCUS[t - 2] - DCEU[t - 2];
//                TPDCUS[t - 1] = DCUS[t - 2];
//                TPDCEU[t - 1] = DCEU[t - 2];
//                TPUSEU[t - 1] = USEU[t - 2];
//                TPEUUS[t - 1] = EUUS[t - 2];
//                USInv[t - 1] = USInv[t - 2] + TPDCUS[t - 2] + TPEUUS[t - 2] - USEU[t - 2] - SalesUS[t - 2];
//                EUInv[t - 1] = EUInv[t - 2] + TPDCEU[t - 2] + TPUSEU[t - 2] - EUUS[t - 2] - SalesEU[t - 2];
//
//                SalesUS[t - 1] = Math.min(DemandUS[t - 1], USInv[t - 1] - USEU[t - 1]);
//                SalesEU[t - 1] = Math.min(DemandEU[t - 1], EUInv[t - 1] - EUUS[t - 1]);
//
//                Prod[t - 1] = eval(input_Prod).value;
//                DCUS[t - 1] = eval(input_transDC2US).value;
//                DCEU[t - 1] = eval(input_transDC2EU).value;
//                USEU[t - 1] = eval(input_transUS2EU).value;
//                EUUS[t - 1] = eval(input_transEU2US).value;
//
//                dis_DCInv.innerHTML = DCInventory[t - 1];
//                dis_tpDCUS.innerHTML = TPDCUS[t - 1];
//                dis_tpDCEU.innerHTML = TPDCEU[t - 1];
//                dis_tpUSEU.innerHTML = TPUSEU[t - 1];
//                dis_tpEUUS.innerHTML = TPEUUS[t - 1];
//                dis_USInv.innerHTML = USInv[t - 1];
//                dis_EUInv.innerHTML = EUInv[t - 1];
//                dis_SalesUS.innerHTML = SalesUS[t - 1];
//                dis_SalesEU.innerHTML = SalesEU[t - 1];
//                dis_DemandUS.innerHTML = DemandUS[t - 1];
//                dis_DemandEU.innerHTML = DemandEU[t - 1];
//
//                Profit[t - 1] = (1 + r) * Profit[t - 2] + priceUS * SalesUS[t - 1] + ExEUROtoUS[t - 1] * priceEU * SalesEU[t - 1] - ExCNYtoUS[t - 1] * CostProd * Prod[t - 1] - CostTranship * (USEU[t - 1] + EUUS[t - 1]);
//                break;
//            }
//        }
//
//        dis_totalProfit.innerHTML = Profit[t - 1];
//
//
//        if(t<N) {
//
//            dis_T.innerHTML++;
//        }
//    }
}
