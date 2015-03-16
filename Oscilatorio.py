# -*- coding: utf-8 -*-
from __future__ import division  #Para que las divisiones den bien!

"""
Created on Wed Feb 25 16:16:04 2015

@author: Ionatan
"""

from Oscilatorio_ui import Ui_MainWindow
import sys
import numpy as np 
import csv

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from PyQt4 import QtGui, QtCore


class Ui_MainWindow_modificada(Ui_MainWindow):

    # Crea variables globales para el programa    
    lista_funciones_guardadas=[]
    tamano_minimo_graficos_x = 400
    tamano_minimo_graficos_y = 100
    MSGERROR='Ha ocurrido un error'    
    TEXTOS={'NADA':'Nada','IDENTIDAD':'Funcion identidad','VELOCIDAD':'Velocidad (m/s)','ACELERACION':'Aceleracion (m/s)^2','ECINETICA':'Energia cinetica (J)','EPOTENCIAL':'Energia potencial (J)','ETOTAL':'Energia total (J)'}
    temporizador=False # Si esta en false muestra los graficos completos
    tiempo=0 # indica hasta q tiempo se debe mostrar los graficos
    marca=0 # se guarda el numero de marca que corresponde al tiempo a mostrar
    
    
    """
        Seccion que redefine cosas del ui para vincularlas a lo que corresponda
    """

    def inicializar(self):
        self.actualizacion_datos_oscilatorio()
        self.quemostrar()
        self.retenidos_quemostrar()
        self.actualizacion_datos()
        
    def conectar(self):
        # Conecta todos los botones que cambian los parametros trigonometricos
        self.control_fase.valueChanged.connect (lambda: self.coordinar_fase(self.control_fase.objectName))
        self.control_fase_grados.valueChanged.connect (lambda: self.coordinar_fase(self.control_fase_grados.objectName))
        self.control_frecuencia_w.valueChanged.connect (lambda: self.coordinar_frecuencia(self.control_frecuencia_w.objectName))
        self.control_frecuencia_hz.valueChanged.connect (lambda: self.coordinar_frecuencia(self.control_frecuencia_hz.objectName))
        self.control_frecuencia_periodo.valueChanged.connect (lambda: self.coordinar_frecuencia(self.control_frecuencia_periodo.objectName))
        self.control_escalaautomatica.clicked.connect (self.coordinar_escala)
        self.control_amplitud.valueChanged.connect(self.actualizacion_datos)
        self.control_x0.valueChanged.connect(self.actualizacion_datos)
        self.control_funcionseno.valueChanged.connect(self.actualizacion_datos)
        # conecta los botones que cambian configuracion de escala
        self.control_escalahorizonalinicio.valueChanged.connect(self.actualizacion_escala)
        self.control_escalahorizontalfin.valueChanged.connect(self.actualizacion_escala)
        self.control_escalavertical.valueChanged.connect(self.actualizacion_escala)
        self.control_escaladensidad.valueChanged.connect(self.actualizacion_escala)
        #Conecta el cambio de tab en la seccion parametros
        self.Parametros.currentChanged.connect(self.evento_cambio_modo)
        #Conecta botones
        self.boton_agregar_acumulado.clicked.connect(self.retenidos_boton_agregar)
        self.boton_editar_acumulado.clicked.connect(self.retenidos_boton_editar)
        self.boton_quitar_acumulado.clicked.connect(self.retenidos_boton_quitar)
        self.boton_limpiar_acumulado.clicked.connect(self.retenidos_boton_limpiar)
        self.boton_acumulados_imagen.clicked.connect(self.retenidos_boton_guardar_imagen)
        self.boton_acumulados_archivo.clicked.connect(self.retenidos_boton_guardar_texto)
        # Conecta controles de parametros oscilatorios
        self.Control_constante_elastica.valueChanged.connect(self.actualizacion_datos)
        self.Control_masa.valueChanged.connect(self.actualizacion_datos)
        self.Control_longitud_natural.valueChanged.connect(self.actualizacion_datos)
        self.Control_posicion_inicial.valueChanged.connect(self.actualizacion_datos)
        self.Control_velocidad_inicial.valueChanged.connect(self.actualizacion_datos)
        self.Control_fuerza_externa.valueChanged.connect(self.actualizacion_datos)
        self.Control_gamma.valueChanged.connect(self.actualizacion_datos)
        # Conecta botones y controles varios
        self.control_envolvente.stateChanged.connect(self.actualizar_graficos)
        self.control_animacion.stateChanged.connect(self.quemostrar)
        self.combo_grafico_secundario.currentIndexChanged.connect(self.evento_mostrar_secundario)
        self.boton_animar.clicked.connect(self.activar_animacion)
        self.boton_animar_detener.clicked.connect(self.detener_animacion)
        # Conecta los menues


    def reemplazar(self):
        # reemplaza el grafico principal
        self.figura_principal=plt.figure()
        self.canvas_principal=FigureCanvas(self.figura_principal)
        self.Grupo_grafico_principal_L.addWidget(self.canvas_principal)
        self.canvas_principal.setMinimumSize(self.tamano_minimo_graficos_x,self.tamano_minimo_graficos_y)
        self.axis_principal = self.figura_principal.add_subplot(111)
        # reemplaza el grafico acumulado
        self.figura_acumulado=plt.figure()
        self.canvas_acumulado=FigureCanvas(self.figura_acumulado)
        self.canvas_acumulado.setMinimumSize(self.tamano_minimo_graficos_x,self.tamano_minimo_graficos_y)        
        self.Grupo_retenidos_v.addWidget(self.canvas_acumulado)
        self.axis_acumulado = self.figura_acumulado.add_subplot(111)
        # agrega grafico secundario
        self.figura_secundaria=plt.figure()
        self.canvas_secundario=FigureCanvas(self.figura_secundaria)
        self.canvas_secundario.setMinimumSize(self.tamano_minimo_graficos_x,self.tamano_minimo_graficos_y)
        self.Grupo_grafico_secundario_L.addWidget(self.canvas_secundario)
        self.axis_secundaria = self.figura_secundaria.add_subplot(111)
        self.canvas_secundario.draw()
        # Agrega grafico animacion
        self.figura_animacion=plt.figure()
        self.canvas_animacion=FigureCanvas(self.figura_animacion)
        self.canvas_animacion.setMinimumSize(200,200) 
        self.Grupo_animacion_L.addWidget(self.canvas_animacion)
        self.axis_animacion= self.figura_animacion.add_subplot(111)
        # Agrega opciones de animacion:
        self.L_botones_animar = QtGui.QHBoxLayout()
        self.boton_animar = QtGui.QPushButton('Animar')
        self.L_botones_animar.addWidget(self.boton_animar)
        self.boton_animar_detener = QtGui.QPushButton('Detener animacion')
        self.L_botones_animar.addWidget(self.boton_animar_detener)
        self.Grupo_animacion_L.addLayout(self.L_botones_animar)
        # Agrega el control de velocidad (tiene cuatro velocidad q corresponden a rapido, medio, lento y muy lento)
        self.L_velocidad_animar = QtGui.QHBoxLayout()
        self.Grupo_animacion_L.addLayout(self.L_velocidad_animar)
        self.label_velocidad_animacion = QtGui.QLabel('Velocidad de animacion:')
        self.L_velocidad_animar.addWidget(self.label_velocidad_animacion)
        self.Control_velocidad_animacion = QtGui.QSpinBox()
        self.Control_velocidad_animacion.setMaximum(3)
        self.Control_velocidad_animacion.setMinimum(1)
        self.Control_velocidad_animacion.setValue(2)
        self.Control_velocidad_animacion.setSingleStep(1)        
        self.L_velocidad_animar.addWidget(self.Control_velocidad_animacion)
        # Completa los menues
        self.infoMenu = self.menubar.addMenu('&Info')
        exitAction = QtGui.QAction('&Exit', self.infoMenu)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Salir de la aplicacion')
        exitAction.triggered.connect(QtGui.qApp.quit)
        aboutAction = QtGui.QAction('Como usar el programa',self.infoMenu)
        aboutAction.setShortcut('Ctrl+U')
        aboutAction.setStatusTip('Informacion general sobre el uso del programa')
        aboutAction.triggered.connect(self.menu_uso)
        creditosAction = QtGui.QAction('Creditos',self.infoMenu)
        creditosAction.setStatusTip('Información acerca del desarrollo del programa')
        creditosAction.triggered.connect(self.menu_creditos)
        tecnicoAction = QtGui.QAction('Detalles tecnicos',self.infoMenu)
        tecnicoAction.setStatusTip(u'Detalle tecnicos de la programación y como ejecutar el programa')
        tecnicoAction.triggered.connect(self.menu_tecnico)
        self.infoMenu.addAction(aboutAction)  
        self.infoMenu.addAction(creditosAction)
        self.infoMenu.addAction(tecnicoAction)
        self.infoMenu.addAction(exitAction)

        # Agrega opciones a combo grafico secundario
        self.combo_grafico_secundario.clear()
        self.combo_grafico_secundario.addItem(self.TEXTOS['NADA'])
        self.combo_grafico_secundario.addItem(self.TEXTOS['IDENTIDAD'])
        self.combo_grafico_secundario.addItem(self.TEXTOS['VELOCIDAD'])
        self.combo_grafico_secundario.addItem(self.TEXTOS['ACELERACION'])        
        self.combo_grafico_secundario.addItem(self.TEXTOS['ECINETICA'])
        self.combo_grafico_secundario.addItem(self.TEXTOS['EPOTENCIAL'])
        self.combo_grafico_secundario.addItem(self.TEXTOS['ETOTAL'])
        
    """
        seccion con lo que deben hacer los eventos
    """    
    
    # eventos que coordinan las diferentes versiones de la misma info
    
    def coordinar_fase(self,origen):
        if origen==self.control_fase.objectName:
            valor=self.control_fase.value() / np.pi *180
            self.control_fase_grados.blockSignals(True)        
            self.control_fase_grados.setValue(valor)
            self.control_fase_grados.blockSignals(False)        
        if origen==self.control_fase_grados.objectName:
            valor=self.control_fase_grados.value() * np.pi / 180
            self.control_fase.blockSignals(True)        
            self.control_fase.setValue(valor)
            self.control_fase.blockSignals(False)  
        
        self.actualizacion_datos()
    
    def coordinar_frecuencia(self,origen):
        
        if origen==self.control_frecuencia_w.objectName:
            valor=self.control_frecuencia_w.value() / (2*np.pi) 
            self.control_frecuencia_hz.blockSignals(True)        
            self.control_frecuencia_hz.setValue(valor)
            self.control_frecuencia_hz.blockSignals(False)        
            if self.control_frecuencia_w.value() == 0: 
                valor = 0
            else:
                valor= 2 * np.pi / self.control_frecuencia_w.value() 
            self.control_frecuencia_periodo.blockSignals(True)        
            self.control_frecuencia_periodo.setValue(valor)
            self.control_frecuencia_periodo.blockSignals(False)        
            
        if origen==self.control_frecuencia_hz.objectName:
            valor=self.control_frecuencia_hz.value() * (2*np.pi) 
            self.control_frecuencia_w.blockSignals(True)        
            self.control_frecuencia_w.setValue(valor)
            self.control_frecuencia_w.blockSignals(False)        
            if self.control_frecuencia_hz.value() == 0: 
                valor = 0
            else:
                valor= 1 / self.control_frecuencia_hz.value() 
            self.control_frecuencia_periodo.blockSignals(True)        
            self.control_frecuencia_periodo.setValue(valor)
            self.control_frecuencia_periodo.blockSignals(False)        
    
        if origen==self.control_frecuencia_periodo.objectName:
            if self.control_frecuencia_periodo.value()==0:
                valor=0
            else:
                valor=(2*np.pi) / self.control_frecuencia_periodo.value()
            self.control_frecuencia_w.blockSignals(True)        
            self.control_frecuencia_w.setValue(valor)
            self.control_frecuencia_w.blockSignals(False)        
            if self.control_frecuencia_periodo.value() == 0: 
                valor = 0
            else:
                valor= 1 / self.control_frecuencia_periodo.value() 
            self.control_frecuencia_hz.blockSignals(True)        
            self.control_frecuencia_hz.setValue(valor)
            self.control_frecuencia_hz.blockSignals(False)      
            
        self.actualizacion_datos()
    
    def coordinar_escala(self):
        if not self.control_escalaautomatica.isChecked():
            self.control_escalavertical.setEnabled(True)
        else:
            self.control_escalavertical.setEnabled(False)
        self.actualizacion_datos()
        
    # muestra u oculta cosas segun corresponda
    def quemostrar (self):
        if self.Parametros.currentIndex()==0 : # La cero es la ventana de trigonometricas
            mostrarsecundario=False
            mostraranimacion=False
        else:
            if self.control_animacion.isChecked(): 
                mostraranimacion=True
                self.actualizar_animacion()
            else:
                mostraranimacion=False
            if self.combo_grafico_secundario.currentText()==self.TEXTOS['NADA']:
                mostrarsecundario=False
            else:
                mostrarsecundario=True
            
        self.Grupo_grafico_secundario.setVisible(mostrarsecundario)
        self.Grupo_animacion.setVisible(mostraranimacion)
        
    
    # eventos que actualizan la info de graficos, listas y formulas    
    def actualizacion_escala(self):
        self.actualizar_graficos()

    def actualizacion_datos(self):
        if self.Parametros.currentIndex()==0 : # La cero es la ventana de trigonometricas
            self.actualizacion_datos_trigonometrica()
        else:
            self.actualizacion_datos_oscilatorio()
        self.actualizar_formula()
        self.actualizar_graficos()

    def actualizacion_datos_oscilatorio(self):
        # Aca esta el nucleo de cuentas fisicas
        # cargamos los datos
        F=self.Control_fuerza_externa.value()
        X0=self.Control_posicion_inicial.value()
        m=self.Control_masa.value()
        V0=self.Control_velocidad_inicial.value()
        L0=self.Control_longitud_natural.value()
        k=self.Control_constante_elastica.value()
        gamma =self.Control_gamma.value()
        # calculamos la posicion de equilibrio
        Xeq = F/k + L0
        # Guardamos el dato
        self.Indicador_equilibrio_sobre.display(Xeq)
        self.Indicador_equilibrio_sub.display(Xeq)
        # calculamos los parametros que salen de la ec. diferencial ma=-kx-gamma*v
        # omitimos F y L0 porque solo afectan el Xeq que ya esta calculado
        # asumimos solucion de la forma x=A*exp(alpha*t)
        # se llega a: m*alpha^2= -k -gamma * alpha
        # si llamamos beta a gamma/2m
        # las soluciones son: -beta +/- sqrt(beta^2 - k/m)
        # donde segun el signo de la raiz es sobre o sub amortiguado
        beta = gamma/(2*m)
        
        # Como a parir de ahora estamos pensando el problema desde la posicion de equilibrio, recalculamos X0
        X0=X0-Xeq
        
        # Determina en que caso de soluciones esta para actuar en consecuencia
        if beta*beta >= k/m:
            self.Solucion_sobreamortiguada=True
        else:
            self.Solucion_sobreamortiguada=False
        
        # muestra el panel de soluciones que corresponda
        self.Grupo_SolucionSub.setVisible(not self.Solucion_sobreamortiguada)
        self.Grupo_SolucionSobre.setVisible(self.Solucion_sobreamortiguada)
        self.control_envolvente.setEnabled(not self.Solucion_sobreamortiguada)
        if self.Solucion_sobreamortiguada:
            self.control_envolvente.setChecked(False)
        
        if self.Solucion_sobreamortiguada:
            # Vamos a tener una solucion de la forma A1*exp(Lambda1*t)+A2*exp(Lambda2*t)
            # Calculamos ambos lambdas
            lambda1 = -beta + np.sqrt(beta*beta-k/m)
            lambda2 = -beta - np.sqrt(beta*beta-k/m)
            # Guardamos los datos
            self.Indicador_lambda1.display(lambda1)
            self.Indicador_lambda2.display(lambda2)
            # Para calcular los A hace falta considerar las condiciones iniciales
            # queda que:
            # X0 = A1 + A2
            # V0 = A1*lambda1 + A2*lambda2
            
            # En caso de la solucion critico lambda1 = lambda2 y A1=A2, y 
            # conviene hacer la cuenta por separado
            
            if beta*beta == k/m: # Caso critico
                # queda: 
                # X0=A1+A2
                # V0=lambda*(A1+A2)
                A1=X0/2
                A2=X0/2
            else:
                A2=(V0-lambda1*X0)/(lambda2-lambda1)
                A1=(V0-lambda2*X0)/(lambda1-lambda2)
                
            # Guardamos los datos
            self.Indicador_A1.display(A1)
            self.Indicador_A2.display(A2)
        else:
            # Estamos en el caso sub amortiguado
            # la raiz es negativa, por lo que podemos sacar un sqrt(-1) de factor comun
            # y si renombramos sqrt(k/m-beta^2)=w queda:
            # A1*exp(-beta+iwt)+A2*exp(-beta-iwt) que se puede reescribir como
            # [A*sen(wt)+B*cos(wt)]*exp(-beta*t)
        
            # Guardamos beta (ya esta calculado)
            self.Indicador_beta.display(beta)
            # Ahora calculamos la solucion de los parametros restantes directamente en su ultima forma
            # Tenemos que:
            # X0 = B 
            # V0 = A*w - B*beta
            
            # Calculamos w y lo guardamos
            w=np.sqrt(k/m-beta*beta)
            self.Indicador_w.display(w)
            
            # Calculamos A y B y los guardamos
            B = X0
            self.Indicador_B.display(B)
            A = (V0 + X0*beta)/w
            self.Indicador_A.display(A)

        # Nota: Hay parametros para los cuales los resultados dan mal, por ej si los parametros k,m o gamma son negativos, o si m=0 o k=0.
        # Se puede chequear que esto no suceda en las cuentas, pero tambien se puede validar automaticamente los valores en la GUI,
        # configurando correctamente los controles. Se ha optado por esto ultimo porque es mas transparente al usuario. 
        
    def actualizacion_datos_trigonometrica(self):
        pass # Por ahora no hay nada especial que hacer cuando se actualizan los datos trigonometricos en particular. 
        # Los eventos de actualizar formula y graficos se activan en la funcion de actualizacion de datos general
        
    def actualizar_graficos(self):
        self.actualizar_grafico_principal()
        self.actualizar_grafico_secundario()
        self.actualizar_animacion()
    
    def actualizar_grafico_principal(self):

        t=self.marca
        # Busca los datos que correspondan
        if self.Parametros.currentIndex()==0 : # La cero es la ventana de trigonometricas
            x_data,y_data = self.calcular_trigonometrica()
        else:
            if self.Solucion_sobreamortiguada:
                x_data,y_data=self.calcular_oscilatoria_sobre()
            else:
                x_data,y_data = self.calcular_oscilatoria_sub()
                if self.control_envolvente.isChecked():
                    x_data_env,y_data_env_mas,y_data_env_menos = self.calcular_oscilatoria_sub_env()
                    if self.temporizador:
                        x_data_env=x_data_env[0:t]
                        y_data_env_mas=y_data_env_mas[0:t]
                        y_data_env_menos=y_data_env_menos[0:t]
             
        if self.temporizador:
            x_data=x_data[0:t]
            y_data=y_data[0:t]
            
        if not hasattr(self, 'linea_grafico_principal'):        
            self.linea_grafico_principal, = self.axis_principal.plot(x_data, y_data)
        else:
            self.linea_grafico_principal.set_xdata(x_data)
            self.linea_grafico_principal.set_ydata(y_data)
        
        if not self.Parametros.currentIndex()==0:
            if self.control_envolvente.isChecked():
                if not hasattr(self, 'linea_grafico_principal_env_mas'):        
                    self.linea_grafico_principal_env_mas, = self.axis_principal.plot(x_data_env, y_data_env_mas,'g--')
                else:
                    self.linea_grafico_principal_env_mas.set_xdata(x_data_env)
                    self.linea_grafico_principal_env_mas.set_ydata(y_data_env_mas)
                
                if not hasattr(self, 'linea_grafico_principal_env_menos'):        
                    self.linea_grafico_principal_env_menos, = self.axis_principal.plot(x_data_env, y_data_env_menos,'g--')
                else:
                    self.linea_grafico_principal_env_menos.set_xdata(x_data_env)
                    self.linea_grafico_principal_env_menos.set_ydata(y_data_env_menos)
            else:
                if hasattr(self, 'linea_grafico_principal_env_menos'):
                    self.linea_grafico_principal_env_menos.remove()
                    delattr (self, 'linea_grafico_principal_env_menos')
                if hasattr(self, 'linea_grafico_principal_env_mas'):
                    self.linea_grafico_principal_env_mas.remove()
                    delattr (self, 'linea_grafico_principal_env_mas')
        else:
            if hasattr(self, 'linea_grafico_principal_env_menos'):
                self.linea_grafico_principal_env_menos.remove()
                delattr (self, 'linea_grafico_principal_env_menos')
            if hasattr(self, 'linea_grafico_principal_env_mas'):
                self.linea_grafico_principal_env_mas.remove()
                delattr (self, 'linea_grafico_principal_env_mas')
                
        if not self.temporizador:
            if self.control_escalaautomatica.isChecked():
                self.axis_principal.relim()
                self.axis_principal.autoscale()
            else:
                y_inicial=-self.control_escalavertical.value()
                y_final=self.control_escalavertical.value()
                self.axis_principal.set_ylim([y_inicial, y_final])
                
        self.canvas_principal.draw()
    
    def actualizar_grafico_secundario(self):
        t=self.marca
        # busca los datos que tenga que mostrar
        if self.combo_grafico_secundario.currentText()==self.TEXTOS['NADA']:
            if hasattr(self, 'linea_grafico_secundario'):
                self.linea_grafico_secundario.remove()
                delattr (self,'linea_grafico_secundario')
        else:
            # busca los datos que tenga que mostrar
            if self.combo_grafico_secundario.currentText()==self.TEXTOS['IDENTIDAD']:
                x_data=self.calcular_ejex()
                y_data=self.calcular_ejex()
                
            if self.combo_grafico_secundario.currentText()==self.TEXTOS['VELOCIDAD']:
                x_data,y_data= self.calcular_velocidad()
                
            if self.combo_grafico_secundario.currentText()==self.TEXTOS['ACELERACION']:
                x_data,y_data= self.calcular_aceleracion()
            
            if self.combo_grafico_secundario.currentText()==self.TEXTOS['ECINETICA']:
                x_data,y_data= self.calcular_energia_cinetica()
                
            if self.combo_grafico_secundario.currentText()==self.TEXTOS['EPOTENCIAL']:
                x_data,y_data= self.calcular_energia_potencial()
                
            if self.combo_grafico_secundario.currentText()==self.TEXTOS['ETOTAL']:
                x_data,y_data= self.calcular_energia_total()

            if self.temporizador:
                x_data=x_data[0:t]
                y_data=y_data[0:t]
            
            if not hasattr(self, 'linea_grafico_secundario'):
                self.linea_grafico_secundario, = self.axis_secundaria.plot(x_data,y_data,'b')
            else:
                self.linea_grafico_secundario.set_xdata(x_data)
                self.linea_grafico_secundario.set_ydata(y_data)
            
            if not self.temporizador:
                self.axis_secundaria.relim()
                self.axis_secundaria.autoscale()
                
            self.canvas_secundario.draw()
    
    # Muestra la formula
    def actualizar_formula(self):
        texto_formula = ''
        if self.Parametros.currentIndex() == 0: #Si esta en modo trigonometrico
            texto_formula += 'f(x)='
            texto_formula += str(self.control_amplitud.value())
            if self.control_funcionseno.value() == 0: # esta en la izq, en sen(x)
                texto_formula += '*sin('
            else:
                texto_formula += '*cos('
            texto_formula += str(self.control_frecuencia_w.value())
            texto_formula += '*t+'
            texto_formula += str(self.control_fase.value())
            texto_formula += ') + '
            texto_formula += str(self.control_x0.value())
        if self.Parametros.currentIndex() == 1: #Si esta en modo oscilatorio
            texto_formula += 'f(x)='
            if self.Solucion_sobreamortiguada:
                texto_formula += str(self.Indicador_A1.value()) + '*exp('
                texto_formula += str(self.Indicador_lambda1.value()) + '*t) +'
                texto_formula += str(self.Indicador_A2.value()) + '*exp('
                texto_formula += str(self.Indicador_lambda2.value()) + '*t) +'
                texto_formula += str(self.Indicador_equilibrio_sobre.value())
            else:
                texto_formula += '['+str(self.Indicador_A.value()) + '*sin('
                texto_formula += str(self.Indicador_w.value()) + '*t) + '
                texto_formula += str(self.Indicador_B.value()) + '*cos('
                texto_formula += str(self.Indicador_w.value()) + '*t)]*exp(-'
                texto_formula += str(self.Indicador_beta.value()) + '*t) + '
                texto_formula += str(self.Indicador_equilibrio_sub.value())
            
        self.etiqueta_formula.setText(texto_formula)

    def actualizar_animacion(self):
        # Nota: esta seccion posee varios parametros de diseno arbitrarios

        # Crea el lienzo
        self.axis_animacion.cla()
        self.axis_animacion.set_xlim([-4,4])
        y_min,y_max=self.axis_principal.get_ylim()
        y_min=y_min-1
        y_max=y_max+1
        if y_max<5: y_max=5
        if y_min>-5: y_min=-5
        self.axis_animacion.set_ylim(y_min,y_max)
        
        # Carga los datos a mostrar
        t=self.marca # Aca se regula q momento muestra
        basura,posicion_t=self.calcular_posicion()
        if t == len(posicion_t): t=t-1
                
        posicion=posicion_t[t]
        L0=self.Control_longitud_natural.value()
        k=self.Control_constante_elastica.value()
        Fext=self.Control_fuerza_externa.value()
        m=self.Control_masa.value()
        basura,velocidad_t=self.calcular_velocidad()
        velocidad=velocidad_t[t]
        basura,aceleracion_t=self.calcular_aceleracion()
        aceleracion=aceleracion_t[t]
        w=self.Indicador_w.value()
        # Genera las lineas del resorte
        lineas=[]
        numero_de_lineas_resorte=10
        numero_de_medialineas=numero_de_lineas_resorte*2
        tramox=0.5
        y_inicio=0
        y_fin=posicion
        tramoy=(y_fin-y_inicio)/numero_de_medialineas
        ancho_linea=0.5
        color='black'
        for n in range(numero_de_medialineas):
            if n % 4 == 0: 
                linea = plt.Line2D((0,tramox), (n*tramoy,(n+1)*tramoy),lw=ancho_linea, color=color)
            if n % 4 == 1: 
                linea = plt.Line2D((tramox,0), (n*tramoy,(n+1)*tramoy),lw=ancho_linea, color=color)
            if n % 4 == 2: 
                linea = plt.Line2D((0,-tramox), (n*tramoy,(n+1)*tramoy), lw=ancho_linea, color=color)
            if n % 4 == 3: 
                linea = plt.Line2D((-tramox,0), (n*tramoy,(n+1)*tramoy), lw=ancho_linea, color=color)
            lineas.append(linea)

        # Dibuja el resorte y las cajita        
        for cadalinea in lineas:
            self.axis_animacion.add_line(cadalinea)
        rectangulo= plt.Rectangle((-tramox,posicion),2*tramox,tramox,fc='blue')        
        self.axis_animacion.add_patch(rectangulo)
        
        # Arma el dibujo de posicion
        if not posicion == 0:            
            self.axis_animacion.arrow(tramox,0,0,posicion,length_includes_head=True,head_width=0.2,head_length=0.2, color='blue')
            if posicion >0: 
                self.axis_animacion.text(0.5,posicion-1,'Posicion',rotation=270,size='smaller')
            else:
                self.axis_animacion.text(0.5,-1,'Posicion',rotation=270,size='smaller')

        # Arma el dibujo de la longitud natural
        self.axis_animacion.add_line(plt.Line2D((-1,-1),(0,L0),lw=ancho_linea, color='black'))
        if not L0==0:
            self.axis_animacion.add_line(plt.Line2D((-1.5,-0.5),(0,0),lw=ancho_linea, color='black'))
            self.axis_animacion.add_line(plt.Line2D((-1.5,-0.5),(L0,L0),lw=ancho_linea, color='black'))
            self.axis_animacion.text(-1,L0-1,'Longitud natural',rotation=270,size='smaller')
            
        # Arma el dibujo de las fuerzas
        
        # Calcula un factor escala para que el valor de la fuerza esperado entre en la pantalla bien. El DCL esta en el medio del liezo
        basura,energia=self.calcular_energia_total()
        energia_maxima=energia[0]
        # Si toda la energia es potencial, 1/2 * k * deltax^2 = E 
        delta_x_max_cuadrado = energia_maxima * 2 / k
        delta_x_max = np.sqrt(delta_x_max_cuadrado)
        fuerza_elastica_maxima = k * delta_x_max
        fuerza_maxima=fuerza_elastica_maxima + Fext
        lugar_disponible = y_max - y_min
        if not fuerza_maxima == 0:
            escala_fuerza = (lugar_disponible/2)/fuerza_maxima
        else:
            escala_fuerza = 0
        
        # Dibuja el cuadrado
        centro_pantalla_y=lugar_disponible/2+y_min
        rectangulo= plt.Rectangle((-3,centro_pantalla_y-0.25),1,0.5,color='black',fill=None)
        self.axis_animacion.add_patch(rectangulo)
        # Dibuja la fuerza elastica
        F_elastica=-k*(posicion-L0)
        longitud_F_elastica=F_elastica*escala_fuerza
        if not longitud_F_elastica == 0:
            self.axis_animacion.arrow(-2.2,centro_pantalla_y,0,longitud_F_elastica,length_includes_head=True,head_width=0.2,head_length=0.1, color='green')
            if F_elastica < 0:
                self.axis_animacion.text(-2.2,centro_pantalla_y-1,'Fuerza elastica',rotation=270,size='smaller',color='green')
            else:
                self.axis_animacion.text(-2.2,centro_pantalla_y+longitud_F_elastica-1,'Fuerza elastica',rotation=270,size='smaller',color='green')
        # Dibuja la fuerza externa        
        longitud_F_fija=Fext*escala_fuerza
        if not longitud_F_fija == 0:
            self.axis_animacion.arrow(-2.8,centro_pantalla_y,0,longitud_F_fija,length_includes_head=True,head_width=0.2,head_length=0.1, color='red')
            if Fext < 0:
                self.axis_animacion.text(-2.8,centro_pantalla_y-1,'Fuerza externa',rotation=270,size='smaller',color='red')
            else:
                self.axis_animacion.text(-2.8,centro_pantalla_y+longitud_F_fija-1,'Fuerza externa',rotation=270,size='smaller',color='red')
        # Dibuja la fuerza total
        fuerza_total=Fext+F_elastica
        longitud_fuerza_total=fuerza_total*escala_fuerza
        if not longitud_fuerza_total == 0:
            self.axis_animacion.arrow(-2.5,centro_pantalla_y,0,longitud_fuerza_total,length_includes_head=True,head_width=0.2,head_length=0.1, color='black')
            if fuerza_total < 0:
                self.axis_animacion.text(-2.5,centro_pantalla_y-1,'Fuerza neta',rotation=270,size='smaller',color='black')
            else:
                self.axis_animacion.text(-2.5,centro_pantalla_y+longitud_fuerza_total-1,'Fuerza neta',rotation=270,size='smaller',color='black')
                
        # Dibuja la velocidad
        velocidad_maxima_cuadrado=energia_maxima*2/m
        velocidad_maxima=np.sqrt(velocidad_maxima_cuadrado)
        if not velocidad_maxima == 0:
            escala_velocidad=(lugar_disponible/2)/velocidad_maxima
        else:
            escala_velocidad=0
        longitud_velocidad=velocidad*escala_velocidad
        if not longitud_velocidad == 0:
            self.axis_animacion.arrow(2,posicion,0,longitud_velocidad,length_includes_head=True,head_width=0.2,head_length=0.1, color='red')
            if velocidad < 0:
                self.axis_animacion.text(2,posicion,'Velocidad',rotation=270,size='smaller',color='red')
            else:
                self.axis_animacion.text(2,posicion+longitud_velocidad,'Velocidad',rotation=270,size='smaller',color='red')
        
        # Dibuja la aceleracion (asume que la escala de aceleracion es v*w)
        escala_aceleracion=escala_velocidad/w        
        longitud_aceleracion=aceleracion*escala_aceleracion
        if not longitud_aceleracion == 0:
            self.axis_animacion.arrow(3,posicion,0,longitud_aceleracion,length_includes_head=True,head_width=0.2,head_length=0.1, color='magenta')
            if aceleracion < 0:
                self.axis_animacion.text(3,posicion,'Aceleracion',rotation=270,size='smaller',color='magenta')
            else:
                self.axis_animacion.text(3,posicion+longitud_aceleracion,'Aceleracion',rotation=270,size='smaller',color='magenta')
        
        self.canvas_animacion.draw()
        
        

    def calcular_trigonometrica(self):
        x_data=self.calcular_ejex()
        # Calcula el eje y        
        y_t_data=x_data*np.array(self.control_frecuencia_w.value()) # w*t
        y_t_data=y_t_data+self.control_fase.value() # wt+phi
        if self.control_funcionseno.value() == 0: # esta en la izq, en sen(x)
            y_t_data=np.sin(y_t_data) # sin (wt+phi)
        else:
            y_t_data=np.cos(y_t_data) # cos (wt+phi)
        y_t_data=y_t_data*self.control_amplitud.value() # A*sin/cos (wt+phi)
        y_t_data=y_t_data+self.control_x0.value() # A sin/cos (wt +phi) +X0
        y_data=y_t_data
        return x_data, y_data
        
    def calcular_posicion(self):
        if self.Solucion_sobreamortiguada:
            x_data,y_data=self.calcular_oscilatoria_sobre()
        else:
            x_data,y_data=self.calcular_oscilatoria_sub()
        return x_data,y_data
    
    def calcular_oscilatoria_sub(self):
        x_data=np.array(self.calcular_ejex())
        y_data_t = self.Indicador_w.value()*x_data # w*t
        y_data_t_A = self.Indicador_A.value() * np.sin(y_data_t)
        y_data_t_B = self.Indicador_B.value() * np.cos(y_data_t)
        y_data_t = y_data_t_A + y_data_t_B
        y_data_t = y_data_t * np.exp(-self.Indicador_beta.value() * x_data)
        y_data=y_data_t + self.Indicador_equilibrio_sub.value()
        return x_data, y_data

    def calcular_oscilatoria_sub_env(self):
        x_data=np.array(self.calcular_ejex())
        y_data_t_mas = self.Indicador_B.value() * np.exp(-self.Indicador_beta.value() * x_data)
        y_data_t_menos = y_data_t_mas * -1
        y_data_mas = y_data_t_mas + self.Indicador_equilibrio_sub.value()
        y_data_menos = y_data_t_menos + self.Indicador_equilibrio_sub.value()
        return x_data, y_data_mas, y_data_menos
        
    def calcular_oscilatoria_sobre(self):
        x_data=np.array(self.calcular_ejex())
        y_data_1=self.Indicador_A1.value()*np.exp(self.Indicador_lambda1.value()*x_data)
        y_data_2=self.Indicador_A2.value()*np.exp(self.Indicador_lambda2.value()*x_data)
        y_data=y_data_1+y_data_2+self.Indicador_equilibrio_sobre.value()
        return x_data, y_data      

    def calcular_ejex(self):
        x_inicial = self.control_escalahorizonalinicio.value()
        x_final = self.control_escalahorizontalfin.value()
        pasos = 10 ** self.control_escaladensidad.value()
        x_datos = np.linspace (x_inicial, x_final, pasos)
        x_datos = x_datos.tolist()
        return x_datos
        
    def calcular_velocidad(self):
        x_data=self.calcular_ejex()
        if self.Solucion_sobreamortiguada:
            # La posicion esta dada por A1*exp(lambda1*t)+A2*exo(lambda2*t)
            # Por ende la velocidad sera:
            # A1*lambda1*exp(lambda1*t)+A2*lambda2*exp(lambda2*t)
            x_data=np.array(self.calcular_ejex())
            y_data_1=self.Indicador_A1.value()*self.Indicador_lambda1.value()*np.exp(self.Indicador_lambda1.value()*x_data)
            y_data_2=self.Indicador_A2.value()*self.Indicador_lambda2.value()*np.exp(self.Indicador_lambda2.value()*x_data)
            y_data=y_data_1+y_data_2
            return x_data,y_data
        else:
            # la posicion esta dada por [A*sin(w*t) + B*cos(w*t)]*exp(-beta*t)
            # por ende la velocidad esta dada por:
            # x(t)*-beta + w*[A*cos(w*t) - B*sin(w*t)]*exp(-beta*t)
            x_basura, y_data_1er_termino=self.calcular_oscilatoria_sub()
            y_data_1er_termino = y_data_1er_termino * -1 * self.Indicador_beta.value()
            x_data=np.array(self.calcular_ejex())
            y_data_t = self.Indicador_w.value()*x_data # w*t
            y_data_t_A = self.Indicador_A.value() * np.cos(y_data_t)
            y_data_t_B = self.Indicador_B.value() * np.sin(y_data_t) * -1
            y_data_t = (y_data_t_A + y_data_t_B)*self.Indicador_w.value()
            y_data_2do_termino = y_data_t * np.exp(-self.Indicador_beta.value() * x_data)
            y_data=y_data_1er_termino + y_data_2do_termino
            return x_data, y_data

    def calcular_aceleracion(self): # ERROR!
        x_data=self.calcular_ejex()
        if self.Solucion_sobreamortiguada:
            # En este caso la solcion es similar a la de velocidad pero salen dos lambdas al derivar dos vees.
            x_data=np.array(self.calcular_ejex())
            y_data_1=self.Indicador_A1.value()*self.Indicador_lambda1.value()*self.Indicador_lambda1.value()*np.exp(self.Indicador_lambda1.value()*x_data)
            y_data_2=self.Indicador_A2.value()*self.Indicador_lambda2.value()*self.Indicador_lambda2.value()*np.exp(self.Indicador_lambda2.value()*x_data)
            y_data=y_data_1+y_data_2
            return x_data,y_data
        else:
            # En el caso sub amortiguado, al derivar dos veces, queda:
            # X(t)*beta^2 - X(t)*w^2 - 2 * [Acos(wt)-Bsin(wt)]*w*beta
            basura, y_data_X = self.calcular_oscilatoria_sub()
            x_data=np.array(self.calcular_ejex())
            y_data_1er_termino=y_data_X*[self.Indicador_beta.value()*self.Indicador_beta.value()-self.Indicador_w.value()*self.Indicador_w.value()]
            y_data_t = self.Indicador_w.value()*x_data # w*t
            y_data_t_A = self.Indicador_A.value() * np.cos(y_data_t)
            y_data_t_B = self.Indicador_B.value() * np.sin(y_data_t)
            y_data_t = (y_data_t_A - y_data_t_B)*self.Indicador_w.value()*self.Indicador_beta.value()
            y_data_2do_termino = y_data_t * np.exp(-self.Indicador_beta.value() * x_data)
            y_data=y_data_1er_termino-2*y_data_2do_termino
            return x_data,y_data       
            
    def calcular_energia_cinetica(self):
        # La energia cinetica es 1/2 * m * v(t)^2
        x_data,y_data_t = self.calcular_velocidad()
        y_data_t = np.array(y_data_t)
        y_data = y_data_t**2 * 0.5 * self.Control_masa.value()
        return x_data,y_data
        
    def calcular_energia_potencial(self):
        # la energia es 1/2 * k * x^2
        x_data,y_data_t = self.calcular_posicion()
        y_data_t = np.array(y_data_t)
        y_data = 0.5 * self.Control_constante_elastica.value() * y_data_t**2
        return x_data,y_data
        
    def calcular_energia_total(self):
        x_data,y_data_cinetica = self.calcular_energia_cinetica()
        x_data,y_data_potencial = self.calcular_energia_potencial()
        y_data = y_data_cinetica + y_data_potencial
        return x_data,y_data        
        
    def retenidos_actualizar(self):
        self.retenidos_actualizar_graficos()
        self.retenidos_actualizar_listado_funciones()
        self.retenidos_quemostrar()        
        
    def retenidos_agregar_funcion_lista(self,nombre,color,estilo,x_data,y_data):
        self.lista_funciones_guardadas.append({'nombre':nombre,'color':color,'estilo':estilo,'x_data':x_data,'y_data':y_data})
        
    def retenidos_actualizar_listado_funciones(self):
        self.combo_retenidos.clear()
        for cadafuncion in self.lista_funciones_guardadas:
            self.combo_retenidos.addItem(cadafuncion['nombre'])

    def retenidos_quitar_funcion(self,nombre):
        for cadagrafico in self.lista_funciones_guardadas:
            if cadagrafico['nombre']==nombre:
                delattr (self, 'linea' + nombre)
                self.lista_funciones_guardadas.remove(cadagrafico)

    def retenidos_actualizar_graficos(self):
        self.axis_acumulado.cla()
        for cadafuncion in self.lista_funciones_guardadas:
            x_data=cadafuncion['x_data']
            y_data=cadafuncion['y_data']
            nombre=cadafuncion['nombre']
            estilo=cadafuncion['estilo']
            color=(cadafuncion['color'][0]/255, cadafuncion['color'][1]/255, cadafuncion['color'][2]/255)
            nombrelinea = 'linea' + nombre
            setattr (self, nombrelinea, self.axis_acumulado.plot(x_data, y_data, estilo, color=color, label=nombre))
        if len(self.lista_funciones_guardadas) > 0:
            self.axis_acumulado.legend(framealpha=0.5)
        self.canvas_acumulado.draw()


    # eventos relacionados a acciones de botones
            
    def retenidos_boton_agregar(self):
        # Primero identifica el origen de los datos
        origen = self.retenidos_determinar_origen()
        if origen==self.MSGERROR: 
            return
            
        # Una vez elegido el origen carga los datos        
        text, ok = QtGui.QInputDialog.getText(QtGui.QInputDialog(), 'Datos para almacenar', 
            'Ingrese un nombre:')
        if ok:
            nombre=text
        else:
            return
            
        for cadafuncion in self.lista_funciones_guardadas:
            if cadafuncion['nombre']==nombre:
                QtGui.QMessageBox.information(None,'Nombre invalido','El nombre ya esta utilizado.')
                return
                
        cuadro_color = QtGui.QColorDialog.getColor()
        if cuadro_color.isValid():
             color = (cuadro_color.red(), cuadro_color.green(), cuadro_color.blue()) 
        lista=['Continua','Punteada','Guiones','Guiones y puntos']
        choice, okPressed = QtGui.QInputDialog.getItem(None, 'Elija un estilo', 'Que tipo de linea desea para el grafico', lista, 0, False)
        if okPressed:
            if choice == 'Continua': estilo = '-'
            if choice == 'Punteada': estilo = ':'
            if choice == 'Guiones': estilo = '--'
            if choice == 'Guiones y puntos': estilo = '-.'
        else:
            return
            
        x_data=origen.get_xdata()
        y_data=origen.get_ydata()
        
        self.retenidos_agregar_funcion_lista (nombre,color,estilo,x_data,y_data)
        self.retenidos_actualizar()
        
    def retenidos_boton_quitar(self):
        self.retenidos_quitar_funcion (self.combo_retenidos.currentText())
        self.retenidos_actualizar()
        
    def retenidos_boton_limpiar(self):
        for cadafuncion in self.lista_funciones_guardadas:
            delattr (self, 'linea' + cadafuncion['nombre'])
            
        self.lista_funciones_guardadas=[]
        self.retenidos_actualizar()
        
        
    def retenidos_boton_guardar_imagen(self):
        lista = ['pdf','png']
        choice, okPressed = QtGui.QInputDialog.getItem(None, 'Formato de archivo', 'Elija en que formato quiere guardar la imagen', lista, 0, False)
        if okPressed:
            extension=choice
        else:
            return
        fileName = QtGui.QFileDialog.getSaveFileName(None, 'Elija donde guardar el archivo...','', extension + ' (*.'+extension+')')
        if not fileName:
            return
        if not extension == fileName[-3:]:
            QtGui.QMessageBox.information(None,'Error','La extension del archivo por crear no coincide con la del tipo de formato que desea guardar. Revise el nombre de archivo elegido.')
        else:
            self.figura_acumulado.savefig(fileName, bbox_inches='tight')
    
    def retenidos_boton_guardar_texto(self):
        if not self.lista_funciones_guardadas:
            QtGui.QMessageBox.information(None,'Advertencia','No hay datos para guardar.')
            return #No hace nada si la lista esta vacia
        datos=[]
        largo = max ([len(cadafuncion['x_data']) for cadafuncion in self.lista_funciones_guardadas])
        largo=largo + 2 # xq hay dos encabezados
        for cadafuncion in self.lista_funciones_guardadas:
            datosx=[cadafuncion['nombre'],'Eje x:']
            datosx.extend(cadafuncion['x_data'])
            datosx.extend(['']*(largo-len(datosx)))
            datosy=[cadafuncion['nombre'],'Eje y:']
            datosy.extend(cadafuncion['y_data'])
            datosy.extend(['']*(largo-len(datosy)))
            datos.append(datosx)
            datos.append(datosy)
        # Extiende las listas en caso de que haya una mas larga que las otras
        datos=[list(i) for i in zip(*datos)] #Traspone los datos para qye se guarden bien
        
        extension='csv'
        fileName = QtGui.QFileDialog.getSaveFileName(None, 'Elija donde guardar el archivo...','', extension + ' (*.'+extension+')')
        if not fileName:
            return
        if not extension == fileName[-3:]:
            QtGui.QMessageBox.information(None,'Error','La extension del archivo por crear no coincide con la del tipo de formato que desea guardar. Revise el nombre de archivo elegido.')
        else:
            with open(fileName, "wb") as f:
                writer = csv.writer(f)
                writer.writerows(datos)

    def retenidos_boton_editar(self):
        nombre_original=self.combo_retenidos.currentText()

        text, ok = QtGui.QInputDialog.getText(QtGui.QInputDialog(), 'Editando el grafico '+nombre_original, 
            'Ingrese un nuevo nombre:')
        if ok:
            nombre=text
        else:
            return
        
        if not nombre_original==nombre:
            for cadafuncion in self.lista_funciones_guardadas:
                if cadafuncion['nombre']==nombre:
                    QtGui.QMessageBox.information(None,'Nombre invalido','El nombre ya esta utilizado.')
                    return        
            
        cuadro_color = QtGui.QColorDialog.getColor()
        if cuadro_color.isValid():
             color = (cuadro_color.red(), cuadro_color.green(), cuadro_color.blue()) 
        
        lista=['Continua','Punteada','Guiones','Guiones y puntos']
        choice, okPressed = QtGui.QInputDialog.getItem(None, 'Elija un nuevo estilo', 'Que tipo de linea desea para el grafico', lista, 0, False)
        if okPressed:
            if choice == 'Continua': estilo = '-'
            if choice == 'Punteada': estilo = ':'
            if choice == 'Guiones': estilo = '--'
            if choice == 'Guiones y puntos': estilo = '-.'
        else:
            return
        
        for cadafuncion in self.lista_funciones_guardadas:
            if cadafuncion['nombre']==nombre_original:
                cadafuncion['nombre']=nombre
                cadafuncion['color']=color
                cadafuncion['estilo']=estilo
        
        self.retenidos_actualizar()
        
    def retenidos_quemostrar(self):
        if not self.lista_funciones_guardadas:
            mostrar=False
        else:
            mostrar=True
        self.boton_acumulados_archivo.setEnabled(mostrar)
        self.boton_acumulados_imagen.setEnabled(mostrar)
        self.boton_editar_acumulado.setEnabled(mostrar)
        self.boton_limpiar_acumulado.setEnabled(mostrar)
        self.boton_quitar_acumulado.setEnabled(mostrar)

    def retenidos_determinar_origen(self):
        lista=[]
        if self.Parametros.currentIndex()==0 : # La cero es la ventana de trigonometricas
            lista.append('Grafico principal')
        else:
            lista.append('Grafico principal')
            if self.control_envolvente.isChecked():
                lista.append('Grafico principal: Envolvente superior')
                lista.append('Grafico principal: Envolvente inferior')
            if not self.combo_grafico_secundario.currentText=='Nada':
                lista.append('Grafico secundario')
        if len (lista) == 1:
            eleccion = lista[0]
        else:
            eleccion, okPressed = QtGui.QInputDialog.getItem(None, 'Origen de datos', 'Elija que desea guardar:', lista, 0, False)
            if not okPressed: 
                origen=self.MSGERROR
                return origen
        if eleccion == 'Grafico principal': origen=self.linea_grafico_principal
        if eleccion == 'Grafico principal: Envolvente superior': origen=self.linea_grafico_principal_env_mas
        if eleccion == 'Grafico principal: Envolvente inferior': origen=self.linea_grafico_principal_env_menos
        if eleccion == 'Grafico secundario': origen=self.linea_grafico_secundario
        return origen
            
    def evento_cambio_modo(self):
        self.quemostrar()
        self.actualizar_formula()
        self.actualizar_graficos()
    
    def evento_mostrar_secundario(self):
        self.quemostrar()
        self.actualizar_grafico_secundario()
    
    def activar_animacion(self):
        self.paso_animacion=0.05  
        if self.Control_velocidad_animacion.value() == 0: 
            self.factor_velocidad=0.01
        if self.Control_velocidad_animacion.value() == 1: 
            self.factor_velocidad=0.1
        if self.Control_velocidad_animacion.value() == 2: 
            self.factor_velocidad=1
        if self.Control_velocidad_animacion.value() == 3: 
            self.factor_velocidad=10
        self.tiempo=self.control_escalahorizonalinicio.value()
        self.temporizador=True
        self.contador=QtCore.QTimer()
        self.contador.timeout.connect(self.procesar_animacion)
        self.Parametros.setEnabled(False)
        self.V_OpcionesEscala.setEnabled(False)
        self.Control_velocidad_animacion.setEnabled(False)
        self.contador.start(self.paso_animacion*1000)
    
    def procesar_animacion(self):
        self.tiempo += self.paso_animacion*self.factor_velocidad
        if self.tiempo > self.control_escalahorizontalfin.value():
            self.temporizador=False # apaga el temporizador
            self.Parametros.setEnabled(True)
            self.V_OpcionesEscala.setEnabled(True)
            self.Control_velocidad_animacion.setEnabled(True)
            self.contador.stop()
            self.marca = 0
            self.actualizar_graficos()
        else:
            self.contador.start(self.paso_animacion*1000)
            # calcula la marca que corresponde a ese tiempo
            delta_tiempo_total = self.control_escalahorizontalfin.value() - self.control_escalahorizonalinicio.value()
            numero_pasos = 10 ** self.control_escaladensidad.value()
            delta_tiempo_paso = delta_tiempo_total / numero_pasos
            self.marca = int((self.tiempo - self.control_escalahorizonalinicio.value())/delta_tiempo_paso)
            self.actualizar_graficos()
        
    def detener_animacion(self):
        self.tiempo = self.control_escalahorizontalfin.value()
        
    def menu_uso(self):
        texto = (u'Este programa esta pensado y diseñado para introducir nociones de problemas oscilatorios. \n \n'
                    u'    Posee una seccion destinada a las funciones trigonometricas propiamente dichas (necesarias '
                    u'para resolver problemas oscilatorios) donde se puede variar los parametros y observar como estos '
                    u'afectan la forma de la funcion y otra seccion en la que se puede introducir parametros fisicos '
                    u'de un problema oscilatorio asociado a un resorte que el programa calcula los parametros de la '
                    u'solución matemática y grafica el resultado.\n'
                    u'    En la seccion oscilatoria se puede elegir ademas de ver el grafico principal (que muestra la '
                    u'posicion en funcion del tiempo) ver otros graficos como velocidad, energia, etc. Tambien se puede '
                    u'optar por incluir una animacion del proceso oscilatorio.\n'
                    u'    En todos los casos se incluye la opcion de acumular cualquiera de los resultados en un mismo '
                    u'gráfico (sección superior derecha) para realizar analisis comparativos. Esta seccion puede ser '
                    u'exportada como imagen, pdf, o archivo de texto para ser procesada o incluida en otro contexto.')
        QtGui.QMessageBox.about(None, 'Como usar el programa', texto)
    
    def menu_creditos(self):
        texto = (u'<html>'
                    u'<center>Oscilatorio V 1.0 </center>'
                    u'<p align="justify"> Este programa fue ideado e implementado originalmente en 2013 el marco de la materia Fisica I '
                    u'(Biologos y Geologos) del departamento de fisica de la facultad de ciencias exactas (Df,FCEN) '
                    u'con el objetivo de realizar una practica computacional para introducir la practica de resortes '
                    u'y problemas oscilatorios. El material original (elaborado en lenguaje MATLAB) puede encontrarse '
                    u'en la página de la materia (http://materias.df.uba.ar/f1bygAa2013c2/novedades/). </p>'
                    u'<p align="justify"> Posteriormente, en base a las limitaciones de la interfaz gráfica del MATLAB, y las mejores '
                    u'caracteristicas que ofrece el lenguaje de programacion Python se rediseño por completo el programa '
                    u'en este lenguaje.</p>'
                    u'<p align="justify">    Esta version del programa fue diseñada y programada por Ionatan Perez (Ionatan@gmail.com) en '
                    u'febrero de 2015, con la colaboración de Francisco Roldan quien ayudo a revisar y corrigir el código '
                    u'correspondiente a los calculos matematicos en numerosas oportunidades.</p>'
                    u'<p align="justify">    Este programa tiene como objetivo servir como complemento a la enseñanza, tanto en cursos universitarios '
                    u'como secundarios. En este sentido se permite su uso, reproducción y modificación libremente siempre y cuando '
                    u'se cite la fuente del material.</p>'
                    u'<p align="justify">    El codigo fuente de este programa se encuentra disponible en https://github.com/IonatanPerez/Oscilatorio '
                    u'Cualquier sugerencia, corrección o error que se desee comunicar es bienvenida ya sea a traves de la pagina o '
                    u'via mail (Ionatan@gmail.com).</p>'
                    u'</html>')
                   
        QtGui.QMessageBox.about(None, 'Acerca del programa', texto)

    def menu_tecnico(self):
        texto = (u'<html>'
                u'<center>Datos técnicos acerca del programa</center>'

                u'<p align="justify"> Si estas leyendo este mensaje en una ventana de texto es porque el programa anda. Puede ser que estes ejecutando '
                u'una version ejecutable (.exe) o bien (lo más probable) que estes compilando el codigo fuente con un interprete '
                u'de Python. Este programa esta escrito en lenguaje Python y se distribuye mediante codigo abierto. Eso significa '
                u'que si tenes una copia del codigo podes verlo, revisarlo y modificarlo a tu gusto. Tambien significa que podes ejecutarlo '
                u'en tu computadora si tenes el interprete de Python, es decir el programa que sabe traducir las instruccion escritas '
                u'en un codigo entendible por humanos en uno entendible por la computadora que estes usando.</p>'
                
                u'<p align="justify"> Para escribir este programa se utilizó el interprete Anaconda que incluye el editor de codigo Spider y muchos de los principales paquetes de instrucciones de Python. '
                u'Tambien se uso PyQt4, un paquete de instrucciones extras que permiten diseñar la interfaz gráfica. Para que este programa corra se debe haber instalado ambos softwares. '
                u'El anaconda se puede <a href=http://continuum.io/downloads>descargar de internet</a> en forma legal y gratuita y es muy facil de instalar. '
                u'Existen diferentes versiones de Python, el presente programa fue escrito en la 2.7, por lo que se debe bajar la version compatible con dicha versión. '
                u'Lo mismo sucede con el PyQt4 que se puede bajar desde su <a href=http://www.riverbankcomputing.co.uk/software/pyqt/download>pagina oficial</a></p>'

                u'<p align="justify"> Una vez instalados ambos programas (las opciones predeterminadas de instalación configuran bien el programa si primero se instala el anaconda y luego el pyqt4), se debe abrir '
                u'en el menu inicio el programa Spider. Con este programa se puede abrir los archivos al igual que con el word se edita un documento de texto.</p>'
                
                u'<p align="justify"> Este programa se distribuye en forma de tres archivos: \'Oscilatorio.py\', \'Oscilatorio.ui\' y \'Oscilatorio_ui.py\'. '
                u'Los archivos \'.py\' poseen codigo de Python, mientras que el diseño grafico se guarda en el archivo \'.ui\'. El archivo principal es el \'Oscilatorio.py\', mientras que \'Oscilatorio_ui.py\' solo tiene '
                u'información de la interfaz grafica en formato de instrucciones de Python. </p>'
                
                u'<p align="justify"> Para mirar y ejecutar este programa se debe abrir el archivo \'Oscilatorio.py\'. Una vez abierto presionando Ctrol+F5 se ejecuta. '
                u'Tenes que tener cuidado de no modificar ninguna linea del programa (salvo que sepas lo que estas haciendo o quieras probar que pasa), porque cualquier modificación afecta el funcionamiento del programa y puede dejar de andar. '
                u'Igual siempre podes volver a bajar la version original del codigo de donde la hayas conseguido.</p>'
                
                u'<p align="justify"> Python es un lenguaje sumamente versatil que permite hacer infinidad de cosas en forma relativamente sencilla. Si te interesa interiorizarte más en como usar este lenguaje '
                u'o tenes alguna duda puntual, podes buscar en internet (hay infinidad de recursos online) o podes buscar el grupo de Python armado por alumnos de la carrera de fisica en <a href=https://www.facebook.com/groups/303815376436624>facebook</a> o la página de <a href=https://talleresfifabsas.wordpress.com>wordpress</a></p>'
             
                u'</html>')
               
        QtGui.QMessageBox.about(None, 'Datos tecnicos', texto)
    
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow_modificada()
ui.setupUi(MainWindow)
ui.reemplazar()
ui.inicializar()
ui.conectar()
MainWindow.show()
sys.exit(app.exec_())
