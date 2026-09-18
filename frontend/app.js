const portfolio={concentration_risk:76,liquidity_risk:82,valuation_risk:71,capital_risk:61,manager_risk:58,macro_risk:63,underlying_asset_risk:67};

async function run(){
  const base=location.hostname==="localhost"||location.hostname==="127.0.0.1" ? "http://localhost:5000" : "http://localhost:5000";
  try{
    const r=await fetch(base+"/api/risk/assess",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(portfolio)});
    if(!r.ok) throw new Error();
    render(await r.json());
  }catch(e){
    renderDemo();
  }
}
function render(data){
  const result=data.result;
  document.querySelector("#score").textContent=result.score;
  document.querySelector("#class").textContent=data.classification;
  document.querySelector("#confidence").textContent=Math.round(data.confidence*100)+"%";
  document.querySelector("#uncertainty").textContent=data.uncertainty;
  document.querySelector("#provenance").textContent=data.provenance.join(" • ");
  document.querySelector("#drivers").innerHTML=data.drivers.map(x=>"<li>"+x+"</li>").join("");
  document.querySelector("#components").innerHTML=Object.entries(result.components).map(([k,v])=>'<div class="metric"><span>'+k.replaceAll("_"," ")+'</span><strong>'+v+'</strong><div class="bar"><i style="width:'+v+'%"></i></div></div>').join("");
}
function renderDemo(){render({result:{score:70,components:portfolio},classification:"HIGH",confidence:.89,uncertainty:"medium",provenance:["sample_portfolio","transparent_weighted_risk_model"],drivers:["Liquidity risk (82)","Concentration risk (76)","Valuation risk (71)"]})}
document.querySelector("#run").addEventListener("click",run);
run();
