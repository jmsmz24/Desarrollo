<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>
<script src="https://code.highcharts.com/modules/export-data.js"></script>
<script src="https://code.highcharts.com/modules/bullet.js"></script>
<script src="https://code.highcharts.com/highcharts-more.js"></script>

<h1>Temperatures</h1>

<!--
<div id="grafico" style="min-width: 500px; height: 500px; margin: 0 auto"></div>
<br>
-->


<script>
/*
cargarGraficos();

function cargarGraficos (){
$.get('index.php?r=temperaturas/getTemp', function (data){
	data = JSON.parse(data);
	console.info(data);
	var datos = [];
	for(var i=0; i < data.length; i++){
		var dato = {
			data: data[i].datos
		}
		datos.push(dato);
	}
	
	Highcharts.chart('grafico', {
		chart: {
			zoomType: 'x'
		},
		title: {
			text: 'Temperatures'
		},

		yAxis: {
			title: {
				text: 'C'
			}
		},
		 xAxis: {
			type:'datetime'
		},
		legend: {
			layout: 'vertical',
			align: 'right',
			verticalAlign: 'middle'
		},

		plotOptions: {
			series: {
				label: {
					connectorAllowed: false
				},
				
			}
		},

		series: datos,

		responsive: {
			rules: [{
				condition: {
					maxWidth: 500
				},
				chartOptions: {
					legend: {
						layout: 'horizontal',
						align: 'center',
						verticalAlign: 'bottom'
					}
				}
			}]
		}

	});

})
}
*/
</script>


<table id="temperaturas">
	<thead>
		 <tr>
			<th>Date</th>
			<th>Core Temperature (C)</th>
			<th>Ambient Temperature (C)</th>
			<th>Humidity (%)</th>
		 </tr>
	</thead>
	<tbody>
		<!-- Contenido de la tabla -->
	</tbody>
</table>

<script>
	$(document).ready(function() {
		$('#temperaturas').DataTable( {
			"order": [[ 0, "desc" ]],
			"ajax": {
				"url": "index.php?r=temperaturas/getTemp",
				"dataSrc": ""
			},
			"columns": [
				{ "data": "fecha" },
				{ "data": "temp" },
				{ "data": "temperature" },
				{ "data": "humidity" }
			]
		} );
	});
	
</script>
