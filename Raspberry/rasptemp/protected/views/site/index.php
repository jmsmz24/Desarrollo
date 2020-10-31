<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name;
?>

<h1><i><?php echo CHtml::encode(Yii::app()->name); ?></i></h1>

<?php
				
					//Fecha actual
					echo date('l jS \of F Y h:i:s A')."</br>";
					echo  " </br>";
					
					//Espacio en la micro SD
					$dst = disk_total_space("/")."</br>";
					$dsf = disk_free_space("/")."</br>";
					echo "Espacio total en MicroSD: ";
					echo round ($dst/1000000000,2). " GB </br>";
					
					echo "Espacio libre en MicroSD: ";
					echo round ($dsf/1000000000,2). " GB </br>";
					
					echo "Espacio usado en MicroSD: ";
					echo round (($dst/1000000000)-($dsf/1000000000),2). " GB </br>";
					
					echo "Porcentaje de espacio disponible en MicroSD: ";
					echo round (($dsf/$dst)*100). " % </br>";
					
					echo  " </br>";
					
					
					//Uso memoria
					echo "Uso de la memoria en esta aplicación: ";
					$ms =  memory_get_usage(); 
					echo round ($ms/1000000,2). " MB </br>";
					
					echo  " </br>";
					/*
					try{
						$conexion = new PDO ('pgsql:host=localhost;dbname=tempsys','pi','raspberry');				
						$statements = $conexion -> prepare('select*from temperaturas order by fecha desc;');
						$statements->execute();
																			
						foreach ($statements as $fila){
							echo $fila['fecha'].' -> '.$fila['temp'].'°C</br>';
						
						}
						
					}catch(PDOException $e){
						echo "Error: ".$e->getMessage();
					}
					*/
			?>
