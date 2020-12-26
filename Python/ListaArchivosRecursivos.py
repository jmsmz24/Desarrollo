import os
import xlrd

#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#####¿DONDE QUIERES QUE SE GUARDEN LAS CARPETAS?###############################
###############################################################################

path = 'D:/prueba/Test/'

################################################################################
###########¿DONDE ESTA EL EXCEL?################################################
################################################################################

path_Excel='D:/prueba/Maestro proyectos DMA.xlsx'

################################################################################
###########¿CON QUE PESTAÑA DEL EXCEL QUIERES TRABAJAR?#########################
################################################################################

pestana = 'Raiz'

################################################################################
#####POSICON DE LOS CAMPOS A PARTIR SE VA A GENERAR EL NOMBRE DE LA CARPETA#####
################################################################################

nombre1 = 5
nombre2 = 7

################################################################################
#############################COMIENZA A GENERARSE###############################

wb = xlrd.open_workbook(path_Excel)
sheet1 = wb.sheet_by_name(pestana)

def crear_directorio (ruta):
    if not os.path.exists(path+nombre_carpeta):
            print (nombre_carpeta)
            os.mkdir(path+nombre_carpeta)
            os.mkdir(path+nombre_carpeta+'/06 PVA Construccion - PVA Mantenimeinto')
            os.mkdir(path+nombre_carpeta+'/07 Especificaciones Ambientales')
            os.mkdir(path+nombre_carpeta+'/08 Incidencias M032')
            os.mkdir(path+nombre_carpeta+'/09 Informes de transferencia mantenimiento')
            os.mkdir(path+nombre_carpeta+'/10 Permisos y Autorizaciones')
            os.mkdir(path+nombre_carpeta+'/11 Restauraciones paisajisticas')
            os.mkdir(path+nombre_carpeta+'/12 Seguimiento ambiental de obra')
            os.mkdir(path+nombre_carpeta+'/13 Otros')

for i in range(sheet1.nrows):
   if i != 0: #Esto es porque no quiero que me itere la priemera fila
        codigo = sheet1.cell_value(i, nombre1)
        instalacion =  sheet1.cell_value(i, nombre2)
        nombre = codigo+" - "+instalacion
        nombre_carpeta = nombre.replace('/','_')
        crear_directorio (path+nombre_carpeta) #Ejecutamos Funcion 
