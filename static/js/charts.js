let _recovered = document.getElementById("recovered").innerHTML;
let _all = document.getElementById("all").innerHTML;
let _deaths = document.getElementById("deaths").innerHTML;
let _active = document.getElementById("active").innerHTML;

//Parse string form HTML to INT without the commas
let all = parseInt(_all.replace(/,/g, ""), 10);
let active = parseInt(_active.replace(/,/g, ""), 10);
let deaths = parseInt(_deaths.replace(/,/g, ""), 10);
let recovered = parseInt(_recovered.replace(/,/g, ""), 10);

let leth_rate = (100 / (all / deaths)).toFixed(1);
let rec_rate = (100 / (all / recovered)).toFixed(1);
let active_rate = (100 / (all / active)).toFixed(1);

var charData = {
  type: "bar",
  backgroundColor: "none",
  title: {
    text: "Estadísticas COVID-19",
    color: "#FFF",
  },
  scaleX: {
    values: ["Recuperados", "Activos", "Muertes", "Totales"],
    lineColor: "#FFF",
    color: "#FFF",

    item: {
      wrapText: true,
      color: "#FFF",
      fontSize: "12",
    },
  },
  series: [
    {
      text: ["Recuperados", "Activos", "Muertes", "Totales"],
      values: [recovered, active, deaths, all],
      backgroundColor: "#58508d #bc5090",
    },
  ],
  plot: {
    animation: {
      effect: "ANIMATION_EXPAND_BOTTOM",
      method: "ANIMATION_STRONG_EASE_OUT",
      sequence: "ANIMATION_BY_NODE",
      speed: 500,
    },
  },
};

zingchart.render({
  id: "myChart",
  data: charData,
  width: "100%",
  height: "100%",
});
