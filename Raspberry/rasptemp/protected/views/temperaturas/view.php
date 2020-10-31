<?php
/* @var $this TemperaturasController */
/* @var $model Temperaturas */

$this->breadcrumbs=array(
	'Temperaturases'=>array('index'),
	$model->id,
);

$this->menu=array(
	array('label'=>'List Temperaturas', 'url'=>array('index')),
	array('label'=>'Create Temperaturas', 'url'=>array('create')),
	array('label'=>'Update Temperaturas', 'url'=>array('update', 'id'=>$model->id)),
	array('label'=>'Delete Temperaturas', 'url'=>'#', 'linkOptions'=>array('submit'=>array('delete','id'=>$model->id),'confirm'=>'Are you sure you want to delete this item?')),
	array('label'=>'Manage Temperaturas', 'url'=>array('admin')),
);
?>

<h1>View Temperaturas #<?php echo $model->id; ?></h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data'=>$model,
	'attributes'=>array(
		'id',
		'fecha',
		'temp',
	),
)); ?>
