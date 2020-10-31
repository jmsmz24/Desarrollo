<?php
/* @var $this TemperaturasController */
/* @var $model Temperaturas */

$this->breadcrumbs=array(
	'Temperaturases'=>array('index'),
	'Create',
);

$this->menu=array(
	array('label'=>'List Temperaturas', 'url'=>array('index')),
	array('label'=>'Manage Temperaturas', 'url'=>array('admin')),
);
?>

<h1>Create Temperaturas</h1>

<?php $this->renderPartial('_form', array('model'=>$model)); ?>