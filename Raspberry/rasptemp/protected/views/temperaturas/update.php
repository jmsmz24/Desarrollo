<?php
/* @var $this TemperaturasController */
/* @var $model Temperaturas */

$this->breadcrumbs=array(
	'Temperaturases'=>array('index'),
	$model->id=>array('view','id'=>$model->id),
	'Update',
);

$this->menu=array(
	array('label'=>'List Temperaturas', 'url'=>array('index')),
	array('label'=>'Create Temperaturas', 'url'=>array('create')),
	array('label'=>'View Temperaturas', 'url'=>array('view', 'id'=>$model->id)),
	array('label'=>'Manage Temperaturas', 'url'=>array('admin')),
);
?>

<h1>Update Temperaturas <?php echo $model->id; ?></h1>

<?php $this->renderPartial('_form', array('model'=>$model)); ?>