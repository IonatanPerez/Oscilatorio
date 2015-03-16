# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Oscilatorio.ui'
#
# Created: Mon Mar 16 13:04:32 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1212, 893)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1192, 832))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.PanelCompleto = QtGui.QVBoxLayout()
        self.PanelCompleto.setObjectName(_fromUtf8("PanelCompleto"))
        self.PanelSuperior = QtGui.QHBoxLayout()
        self.PanelSuperior.setObjectName(_fromUtf8("PanelSuperior"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.Parametros = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.Parametros.setObjectName(_fromUtf8("Parametros"))
        self.ParametrosTrigonometricos = QtGui.QWidget()
        self.ParametrosTrigonometricos.setObjectName(_fromUtf8("ParametrosTrigonometricos"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.ParametrosTrigonometricos)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.VentanaPrincipal = QtGui.QVBoxLayout()
        self.VentanaPrincipal.setObjectName(_fromUtf8("VentanaPrincipal"))
        self.V_amplitud = QtGui.QHBoxLayout()
        self.V_amplitud.setObjectName(_fromUtf8("V_amplitud"))
        self.control_amplitud = QtGui.QDoubleSpinBox(self.ParametrosTrigonometricos)
        self.control_amplitud.setProperty("value", 1.0)
        self.control_amplitud.setObjectName(_fromUtf8("control_amplitud"))
        self.V_amplitud.addWidget(self.control_amplitud)
        self.label = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label.setObjectName(_fromUtf8("label"))
        self.V_amplitud.addWidget(self.label)
        self.VentanaPrincipal.addLayout(self.V_amplitud)
        self.V_frecuencia = QtGui.QHBoxLayout()
        self.V_frecuencia.setObjectName(_fromUtf8("V_frecuencia"))
        self.control_frecuencia_w = QtGui.QDoubleSpinBox(self.ParametrosTrigonometricos)
        self.control_frecuencia_w.setProperty("value", 1.0)
        self.control_frecuencia_w.setObjectName(_fromUtf8("control_frecuencia_w"))
        self.V_frecuencia.addWidget(self.control_frecuencia_w)
        self.label_8 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.V_frecuencia.addWidget(self.label_8)
        self.control_frecuencia_hz = QtGui.QDoubleSpinBox(self.ParametrosTrigonometricos)
        self.control_frecuencia_hz.setProperty("value", 0.16)
        self.control_frecuencia_hz.setObjectName(_fromUtf8("control_frecuencia_hz"))
        self.V_frecuencia.addWidget(self.control_frecuencia_hz)
        self.label_7 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.V_frecuencia.addWidget(self.label_7)
        self.control_frecuencia_periodo = QtGui.QDoubleSpinBox(self.ParametrosTrigonometricos)
        self.control_frecuencia_periodo.setProperty("value", 6.28)
        self.control_frecuencia_periodo.setObjectName(_fromUtf8("control_frecuencia_periodo"))
        self.V_frecuencia.addWidget(self.control_frecuencia_periodo)
        self.label_9 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.V_frecuencia.addWidget(self.label_9)
        self.VentanaPrincipal.addLayout(self.V_frecuencia)
        self.V_Fase = QtGui.QHBoxLayout()
        self.V_Fase.setObjectName(_fromUtf8("V_Fase"))
        self.control_fase_grados = QtGui.QDoubleSpinBox(self.ParametrosTrigonometricos)
        self.control_fase_grados.setMinimum(-360.0)
        self.control_fase_grados.setMaximum(360.0)
        self.control_fase_grados.setObjectName(_fromUtf8("control_fase_grados"))
        self.V_Fase.addWidget(self.control_fase_grados)
        self.label_6 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.V_Fase.addWidget(self.label_6)
        self.control_fase = QtGui.QDoubleSpinBox(self.ParametrosTrigonometricos)
        self.control_fase.setMinimum(-6.28)
        self.control_fase.setMaximum(6.28)
        self.control_fase.setSingleStep(0.01)
        self.control_fase.setObjectName(_fromUtf8("control_fase"))
        self.V_Fase.addWidget(self.control_fase)
        self.label_2 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.V_Fase.addWidget(self.label_2)
        self.VentanaPrincipal.addLayout(self.V_Fase)
        self.V_terminoindependiente = QtGui.QHBoxLayout()
        self.V_terminoindependiente.setObjectName(_fromUtf8("V_terminoindependiente"))
        self.control_x0 = QtGui.QDoubleSpinBox(self.ParametrosTrigonometricos)
        self.control_x0.setMinimum(-100.0)
        self.control_x0.setMaximum(100.0)
        self.control_x0.setObjectName(_fromUtf8("control_x0"))
        self.V_terminoindependiente.addWidget(self.control_x0)
        self.label_10 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.V_terminoindependiente.addWidget(self.label_10)
        self.VentanaPrincipal.addLayout(self.V_terminoindependiente)
        self.V_Sin_Cos = QtGui.QHBoxLayout()
        self.V_Sin_Cos.setObjectName(_fromUtf8("V_Sin_Cos"))
        self.label_11 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.V_Sin_Cos.addWidget(self.label_11)
        self.control_funcionseno = QtGui.QSlider(self.ParametrosTrigonometricos)
        self.control_funcionseno.setMaximum(1)
        self.control_funcionseno.setOrientation(QtCore.Qt.Horizontal)
        self.control_funcionseno.setObjectName(_fromUtf8("control_funcionseno"))
        self.V_Sin_Cos.addWidget(self.control_funcionseno)
        self.label_12 = QtGui.QLabel(self.ParametrosTrigonometricos)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.V_Sin_Cos.addWidget(self.label_12)
        self.VentanaPrincipal.addLayout(self.V_Sin_Cos)
        self.horizontalLayout_4.addLayout(self.VentanaPrincipal)
        self.Parametros.addTab(self.ParametrosTrigonometricos, _fromUtf8(""))
        self.ParametrosOscilatorio = QtGui.QWidget()
        self.ParametrosOscilatorio.setObjectName(_fromUtf8("ParametrosOscilatorio"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.ParametrosOscilatorio)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.V_organizaroOsci = QtGui.QHBoxLayout()
        self.V_organizaroOsci.setObjectName(_fromUtf8("V_organizaroOsci"))
        self.Grupo_parametrosFisicos = QtGui.QGroupBox(self.ParametrosOscilatorio)
        self.Grupo_parametrosFisicos.setObjectName(_fromUtf8("Grupo_parametrosFisicos"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Grupo_parametrosFisicos)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.Grupo_parametrosFisicos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.Control_constante_elastica = QtGui.QDoubleSpinBox(self.Grupo_parametrosFisicos)
        self.Control_constante_elastica.setMinimum(0.01)
        self.Control_constante_elastica.setMaximum(100000.0)
        self.Control_constante_elastica.setSingleStep(1.0)
        self.Control_constante_elastica.setProperty("value", 100.0)
        self.Control_constante_elastica.setObjectName(_fromUtf8("Control_constante_elastica"))
        self.verticalLayout_4.addWidget(self.Control_constante_elastica)
        self.label_16 = QtGui.QLabel(self.Grupo_parametrosFisicos)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_4.addWidget(self.label_16)
        self.Control_masa = QtGui.QDoubleSpinBox(self.Grupo_parametrosFisicos)
        self.Control_masa.setMinimum(0.01)
        self.Control_masa.setMaximum(10000.0)
        self.Control_masa.setProperty("value", 10.0)
        self.Control_masa.setObjectName(_fromUtf8("Control_masa"))
        self.verticalLayout_4.addWidget(self.Control_masa)
        self.label_17 = QtGui.QLabel(self.Grupo_parametrosFisicos)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_4.addWidget(self.label_17)
        self.Control_longitud_natural = QtGui.QDoubleSpinBox(self.Grupo_parametrosFisicos)
        self.Control_longitud_natural.setMaximum(100.0)
        self.Control_longitud_natural.setProperty("value", 0.0)
        self.Control_longitud_natural.setObjectName(_fromUtf8("Control_longitud_natural"))
        self.verticalLayout_4.addWidget(self.Control_longitud_natural)
        self.label_18 = QtGui.QLabel(self.Grupo_parametrosFisicos)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_4.addWidget(self.label_18)
        self.Control_posicion_inicial = QtGui.QDoubleSpinBox(self.Grupo_parametrosFisicos)
        self.Control_posicion_inicial.setMinimum(-100.0)
        self.Control_posicion_inicial.setMaximum(100.0)
        self.Control_posicion_inicial.setProperty("value", 1.0)
        self.Control_posicion_inicial.setObjectName(_fromUtf8("Control_posicion_inicial"))
        self.verticalLayout_4.addWidget(self.Control_posicion_inicial)
        self.label_19 = QtGui.QLabel(self.Grupo_parametrosFisicos)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_4.addWidget(self.label_19)
        self.Control_velocidad_inicial = QtGui.QDoubleSpinBox(self.Grupo_parametrosFisicos)
        self.Control_velocidad_inicial.setMinimum(-100.0)
        self.Control_velocidad_inicial.setMaximum(100.0)
        self.Control_velocidad_inicial.setObjectName(_fromUtf8("Control_velocidad_inicial"))
        self.verticalLayout_4.addWidget(self.Control_velocidad_inicial)
        self.label_20 = QtGui.QLabel(self.Grupo_parametrosFisicos)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_4.addWidget(self.label_20)
        self.Control_fuerza_externa = QtGui.QDoubleSpinBox(self.Grupo_parametrosFisicos)
        self.Control_fuerza_externa.setMinimum(-100.0)
        self.Control_fuerza_externa.setMaximum(100.0)
        self.Control_fuerza_externa.setObjectName(_fromUtf8("Control_fuerza_externa"))
        self.verticalLayout_4.addWidget(self.Control_fuerza_externa)
        self.label_33 = QtGui.QLabel(self.Grupo_parametrosFisicos)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.verticalLayout_4.addWidget(self.label_33)
        self.Control_gamma = QtGui.QDoubleSpinBox(self.Grupo_parametrosFisicos)
        self.Control_gamma.setMaximum(100.0)
        self.Control_gamma.setObjectName(_fromUtf8("Control_gamma"))
        self.verticalLayout_4.addWidget(self.Control_gamma)
        self.V_organizaroOsci.addWidget(self.Grupo_parametrosFisicos)
        self.Grupo_SolucionSub = QtGui.QGroupBox(self.ParametrosOscilatorio)
        self.Grupo_SolucionSub.setObjectName(_fromUtf8("Grupo_SolucionSub"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Grupo_SolucionSub)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_21 = QtGui.QLabel(self.Grupo_SolucionSub)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_5.addWidget(self.label_21)
        self.Indicador_A = QtGui.QLCDNumber(self.Grupo_SolucionSub)
        self.Indicador_A.setProperty("value", 0.0)
        self.Indicador_A.setObjectName(_fromUtf8("Indicador_A"))
        self.verticalLayout_5.addWidget(self.Indicador_A)
        self.label_25 = QtGui.QLabel(self.Grupo_SolucionSub)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.verticalLayout_5.addWidget(self.label_25)
        self.Indicador_B = QtGui.QLCDNumber(self.Grupo_SolucionSub)
        self.Indicador_B.setObjectName(_fromUtf8("Indicador_B"))
        self.verticalLayout_5.addWidget(self.Indicador_B)
        self.label_24 = QtGui.QLabel(self.Grupo_SolucionSub)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_5.addWidget(self.label_24)
        self.Indicador_w = QtGui.QLCDNumber(self.Grupo_SolucionSub)
        self.Indicador_w.setObjectName(_fromUtf8("Indicador_w"))
        self.verticalLayout_5.addWidget(self.Indicador_w)
        self.label_27 = QtGui.QLabel(self.Grupo_SolucionSub)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.verticalLayout_5.addWidget(self.label_27)
        self.Indicador_beta = QtGui.QLCDNumber(self.Grupo_SolucionSub)
        self.Indicador_beta.setObjectName(_fromUtf8("Indicador_beta"))
        self.verticalLayout_5.addWidget(self.Indicador_beta)
        self.label_31 = QtGui.QLabel(self.Grupo_SolucionSub)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.verticalLayout_5.addWidget(self.label_31)
        self.Indicador_equilibrio_sub = QtGui.QLCDNumber(self.Grupo_SolucionSub)
        self.Indicador_equilibrio_sub.setObjectName(_fromUtf8("Indicador_equilibrio_sub"))
        self.verticalLayout_5.addWidget(self.Indicador_equilibrio_sub)
        self.V_organizaroOsci.addWidget(self.Grupo_SolucionSub)
        self.Grupo_SolucionSobre = QtGui.QGroupBox(self.ParametrosOscilatorio)
        self.Grupo_SolucionSobre.setObjectName(_fromUtf8("Grupo_SolucionSobre"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.Grupo_SolucionSobre)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_22 = QtGui.QLabel(self.Grupo_SolucionSobre)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_8.addWidget(self.label_22)
        self.Indicador_A1 = QtGui.QLCDNumber(self.Grupo_SolucionSobre)
        self.Indicador_A1.setObjectName(_fromUtf8("Indicador_A1"))
        self.verticalLayout_8.addWidget(self.Indicador_A1)
        self.label_23 = QtGui.QLabel(self.Grupo_SolucionSobre)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_8.addWidget(self.label_23)
        self.Indicador_lambda1 = QtGui.QLCDNumber(self.Grupo_SolucionSobre)
        self.Indicador_lambda1.setObjectName(_fromUtf8("Indicador_lambda1"))
        self.verticalLayout_8.addWidget(self.Indicador_lambda1)
        self.label_28 = QtGui.QLabel(self.Grupo_SolucionSobre)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout_8.addWidget(self.label_28)
        self.Indicador_A2 = QtGui.QLCDNumber(self.Grupo_SolucionSobre)
        self.Indicador_A2.setObjectName(_fromUtf8("Indicador_A2"))
        self.verticalLayout_8.addWidget(self.Indicador_A2)
        self.label_29 = QtGui.QLabel(self.Grupo_SolucionSobre)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.verticalLayout_8.addWidget(self.label_29)
        self.Indicador_lambda2 = QtGui.QLCDNumber(self.Grupo_SolucionSobre)
        self.Indicador_lambda2.setObjectName(_fromUtf8("Indicador_lambda2"))
        self.verticalLayout_8.addWidget(self.Indicador_lambda2)
        self.label_32 = QtGui.QLabel(self.Grupo_SolucionSobre)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.verticalLayout_8.addWidget(self.label_32)
        self.Indicador_equilibrio_sobre = QtGui.QLCDNumber(self.Grupo_SolucionSobre)
        self.Indicador_equilibrio_sobre.setObjectName(_fromUtf8("Indicador_equilibrio_sobre"))
        self.verticalLayout_8.addWidget(self.Indicador_equilibrio_sobre)
        self.V_organizaroOsci.addWidget(self.Grupo_SolucionSobre)
        self.verticalLayout_7.addLayout(self.V_organizaroOsci)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_30 = QtGui.QLabel(self.ParametrosOscilatorio)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_6.addWidget(self.label_30)
        self.combo_grafico_secundario = QtGui.QComboBox(self.ParametrosOscilatorio)
        self.combo_grafico_secundario.setObjectName(_fromUtf8("combo_grafico_secundario"))
        self.combo_grafico_secundario.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.combo_grafico_secundario)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.control_animacion = QtGui.QCheckBox(self.ParametrosOscilatorio)
        self.control_animacion.setObjectName(_fromUtf8("control_animacion"))
        self.horizontalLayout_5.addWidget(self.control_animacion)
        self.control_envolvente = QtGui.QCheckBox(self.ParametrosOscilatorio)
        self.control_envolvente.setObjectName(_fromUtf8("control_envolvente"))
        self.horizontalLayout_5.addWidget(self.control_envolvente)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.Parametros.addTab(self.ParametrosOscilatorio, _fromUtf8(""))
        self.verticalLayout_11.addWidget(self.Parametros)
        self.V_OpcionesEscala = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.V_OpcionesEscala.setObjectName(_fromUtf8("V_OpcionesEscala"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.V_OpcionesEscala)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.V_SubEscala = QtGui.QVBoxLayout()
        self.V_SubEscala.setObjectName(_fromUtf8("V_SubEscala"))
        self.V_EscalaVertical = QtGui.QHBoxLayout()
        self.V_EscalaVertical.setObjectName(_fromUtf8("V_EscalaVertical"))
        self.control_escalaautomatica = QtGui.QCheckBox(self.V_OpcionesEscala)
        self.control_escalaautomatica.setChecked(True)
        self.control_escalaautomatica.setObjectName(_fromUtf8("control_escalaautomatica"))
        self.V_EscalaVertical.addWidget(self.control_escalaautomatica)
        self.label_15 = QtGui.QLabel(self.V_OpcionesEscala)
        self.label_15.setEnabled(True)
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.V_EscalaVertical.addWidget(self.label_15, QtCore.Qt.AlignRight)
        self.control_escalavertical = QtGui.QSpinBox(self.V_OpcionesEscala)
        self.control_escalavertical.setEnabled(False)
        self.control_escalavertical.setMinimum(1)
        self.control_escalavertical.setProperty("value", 1)
        self.control_escalavertical.setObjectName(_fromUtf8("control_escalavertical"))
        self.V_EscalaVertical.addWidget(self.control_escalavertical)
        self.label_5 = QtGui.QLabel(self.V_OpcionesEscala)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.V_EscalaVertical.addWidget(self.label_5)
        self.V_SubEscala.addLayout(self.V_EscalaVertical)
        self.v_EscalaHorizonatal = QtGui.QHBoxLayout()
        self.v_EscalaHorizonatal.setObjectName(_fromUtf8("v_EscalaHorizonatal"))
        self.control_escalahorizonalinicio = QtGui.QDoubleSpinBox(self.V_OpcionesEscala)
        self.control_escalahorizonalinicio.setDecimals(1)
        self.control_escalahorizonalinicio.setMinimum(-1000.0)
        self.control_escalahorizonalinicio.setMaximum(1000.0)
        self.control_escalahorizonalinicio.setObjectName(_fromUtf8("control_escalahorizonalinicio"))
        self.v_EscalaHorizonatal.addWidget(self.control_escalahorizonalinicio)
        self.label_13 = QtGui.QLabel(self.V_OpcionesEscala)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.v_EscalaHorizonatal.addWidget(self.label_13)
        self.control_escalahorizontalfin = QtGui.QDoubleSpinBox(self.V_OpcionesEscala)
        self.control_escalahorizontalfin.setDecimals(1)
        self.control_escalahorizontalfin.setMinimum(-1000.0)
        self.control_escalahorizontalfin.setMaximum(1000.0)
        self.control_escalahorizontalfin.setProperty("value", 10.0)
        self.control_escalahorizontalfin.setObjectName(_fromUtf8("control_escalahorizontalfin"))
        self.v_EscalaHorizonatal.addWidget(self.control_escalahorizontalfin)
        self.label_14 = QtGui.QLabel(self.V_OpcionesEscala)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.v_EscalaHorizonatal.addWidget(self.label_14)
        self.control_escaladensidad = QtGui.QSpinBox(self.V_OpcionesEscala)
        self.control_escaladensidad.setMinimum(1)
        self.control_escaladensidad.setMaximum(5)
        self.control_escaladensidad.setProperty("value", 3)
        self.control_escaladensidad.setObjectName(_fromUtf8("control_escaladensidad"))
        self.v_EscalaHorizonatal.addWidget(self.control_escaladensidad)
        self.label_3 = QtGui.QLabel(self.V_OpcionesEscala)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.v_EscalaHorizonatal.addWidget(self.label_3)
        self.V_SubEscala.addLayout(self.v_EscalaHorizonatal)
        self.verticalLayout_3.addLayout(self.V_SubEscala)
        self.verticalLayout_11.addWidget(self.V_OpcionesEscala)
        self.PanelSuperior.addLayout(self.verticalLayout_11)
        self.PanelGraficosAcumulados = QtGui.QVBoxLayout()
        self.PanelGraficosAcumulados.setObjectName(_fromUtf8("PanelGraficosAcumulados"))
        self.Grupo_retenidos = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Grupo_retenidos.sizePolicy().hasHeightForWidth())
        self.Grupo_retenidos.setSizePolicy(sizePolicy)
        self.Grupo_retenidos.setObjectName(_fromUtf8("Grupo_retenidos"))
        self.Grupo_retenidos_v = QtGui.QHBoxLayout(self.Grupo_retenidos)
        self.Grupo_retenidos_v.setObjectName(_fromUtf8("Grupo_retenidos_v"))
        self.PanelGraficosAcumulados.addWidget(self.Grupo_retenidos)
        self.PanelgraficoAcumuadoBotones = QtGui.QHBoxLayout()
        self.PanelgraficoAcumuadoBotones.setObjectName(_fromUtf8("PanelgraficoAcumuadoBotones"))
        self.combo_retenidos = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.combo_retenidos.setObjectName(_fromUtf8("combo_retenidos"))
        self.PanelgraficoAcumuadoBotones.addWidget(self.combo_retenidos)
        self.boton_agregar_acumulado = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.boton_agregar_acumulado.setObjectName(_fromUtf8("boton_agregar_acumulado"))
        self.PanelgraficoAcumuadoBotones.addWidget(self.boton_agregar_acumulado)
        self.boton_editar_acumulado = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.boton_editar_acumulado.setObjectName(_fromUtf8("boton_editar_acumulado"))
        self.PanelgraficoAcumuadoBotones.addWidget(self.boton_editar_acumulado)
        self.boton_quitar_acumulado = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_quitar_acumulado.sizePolicy().hasHeightForWidth())
        self.boton_quitar_acumulado.setSizePolicy(sizePolicy)
        self.boton_quitar_acumulado.setObjectName(_fromUtf8("boton_quitar_acumulado"))
        self.PanelgraficoAcumuadoBotones.addWidget(self.boton_quitar_acumulado)
        self.boton_limpiar_acumulado = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.boton_limpiar_acumulado.setObjectName(_fromUtf8("boton_limpiar_acumulado"))
        self.PanelgraficoAcumuadoBotones.addWidget(self.boton_limpiar_acumulado)
        self.boton_acumulados_imagen = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.boton_acumulados_imagen.setObjectName(_fromUtf8("boton_acumulados_imagen"))
        self.PanelgraficoAcumuadoBotones.addWidget(self.boton_acumulados_imagen)
        self.boton_acumulados_archivo = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.boton_acumulados_archivo.setObjectName(_fromUtf8("boton_acumulados_archivo"))
        self.PanelgraficoAcumuadoBotones.addWidget(self.boton_acumulados_archivo)
        self.PanelGraficosAcumulados.addLayout(self.PanelgraficoAcumuadoBotones)
        self.PanelSuperior.addLayout(self.PanelGraficosAcumulados)
        self.PanelSuperior.setStretch(1, 1)
        self.PanelCompleto.addLayout(self.PanelSuperior)
        self.Grupo_formula = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.Grupo_formula.setObjectName(_fromUtf8("Grupo_formula"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Grupo_formula)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.etiqueta_formula = QtGui.QLabel(self.Grupo_formula)
        self.etiqueta_formula.setAlignment(QtCore.Qt.AlignCenter)
        self.etiqueta_formula.setObjectName(_fromUtf8("etiqueta_formula"))
        self.verticalLayout.addWidget(self.etiqueta_formula)
        self.PanelCompleto.addWidget(self.Grupo_formula)
        self.Grupo_graficos_animaciones = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Grupo_graficos_animaciones.sizePolicy().hasHeightForWidth())
        self.Grupo_graficos_animaciones.setSizePolicy(sizePolicy)
        self.Grupo_graficos_animaciones.setObjectName(_fromUtf8("Grupo_graficos_animaciones"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.Grupo_graficos_animaciones)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.Grupo_animacion = QtGui.QGroupBox(self.Grupo_graficos_animaciones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Grupo_animacion.sizePolicy().hasHeightForWidth())
        self.Grupo_animacion.setSizePolicy(sizePolicy)
        self.Grupo_animacion.setObjectName(_fromUtf8("Grupo_animacion"))
        self.Grupo_animacion_L = QtGui.QVBoxLayout(self.Grupo_animacion)
        self.Grupo_animacion_L.setObjectName(_fromUtf8("Grupo_animacion_L"))
        self.horizontalLayout_7.addWidget(self.Grupo_animacion)
        self.Grupo_graficos = QtGui.QGroupBox(self.Grupo_graficos_animaciones)
        self.Grupo_graficos.setObjectName(_fromUtf8("Grupo_graficos"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.Grupo_graficos)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.Grupo_grafico_principal = QtGui.QGroupBox(self.Grupo_graficos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Grupo_grafico_principal.sizePolicy().hasHeightForWidth())
        self.Grupo_grafico_principal.setSizePolicy(sizePolicy)
        self.Grupo_grafico_principal.setObjectName(_fromUtf8("Grupo_grafico_principal"))
        self.Grupo_grafico_principal_L = QtGui.QVBoxLayout(self.Grupo_grafico_principal)
        self.Grupo_grafico_principal_L.setSpacing(0)
        self.Grupo_grafico_principal_L.setMargin(0)
        self.Grupo_grafico_principal_L.setObjectName(_fromUtf8("Grupo_grafico_principal_L"))
        self.verticalLayout_10.addWidget(self.Grupo_grafico_principal)
        self.Grupo_grafico_secundario = QtGui.QGroupBox(self.Grupo_graficos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Grupo_grafico_secundario.sizePolicy().hasHeightForWidth())
        self.Grupo_grafico_secundario.setSizePolicy(sizePolicy)
        self.Grupo_grafico_secundario.setObjectName(_fromUtf8("Grupo_grafico_secundario"))
        self.Grupo_grafico_secundario_L = QtGui.QHBoxLayout(self.Grupo_grafico_secundario)
        self.Grupo_grafico_secundario_L.setSpacing(0)
        self.Grupo_grafico_secundario_L.setMargin(0)
        self.Grupo_grafico_secundario_L.setObjectName(_fromUtf8("Grupo_grafico_secundario_L"))
        self.verticalLayout_10.addWidget(self.Grupo_grafico_secundario)
        self.horizontalLayout_7.addWidget(self.Grupo_graficos)
        self.PanelCompleto.addWidget(self.Grupo_graficos_animaciones)
        self.PanelCompleto.setStretch(0, 20)
        self.horizontalLayout_3.addLayout(self.PanelCompleto)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1212, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Parametros.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Amplitud", None))
        self.label_8.setText(_translate("MainWindow", "Frecuencia (rad/s)", None))
        self.label_7.setText(_translate("MainWindow", "Frecuencia (hz)", None))
        self.label_9.setText(_translate("MainWindow", "Periodo", None))
        self.label_6.setText(_translate("MainWindow", "Fase Inicial (grados)", None))
        self.label_2.setText(_translate("MainWindow", "Fase inicial (rad)", None))
        self.label_10.setText(_translate("MainWindow", "Termino independiente", None))
        self.label_11.setText(_translate("MainWindow", "Sin (x)", None))
        self.label_12.setText(_translate("MainWindow", "Cos(x)", None))
        self.Parametros.setTabText(self.Parametros.indexOf(self.ParametrosTrigonometricos), _translate("MainWindow", "Funcion Trigonometrica", None))
        self.Grupo_parametrosFisicos.setTitle(_translate("MainWindow", "Parametros fisicos", None))
        self.label_4.setText(_translate("MainWindow", "Constante elastica (N/m)", None))
        self.label_16.setText(_translate("MainWindow", "Masa (Kg)", None))
        self.label_17.setText(_translate("MainWindow", "Longitud natural (m)", None))
        self.label_18.setText(_translate("MainWindow", "Posicion inicial (m)", None))
        self.label_19.setText(_translate("MainWindow", "Velocidad inicial (m/s)", None))
        self.label_20.setText(_translate("MainWindow", "Fuerzas externas fijas (N)", None))
        self.label_33.setText(_translate("MainWindow", "Cte. de amort. (Kg/s)", None))
        self.Grupo_SolucionSub.setTitle(_translate("MainWindow", "Solucion sub amortiguada", None))
        self.label_21.setText(_translate("MainWindow", "Amplitud (Sin) (m):", None))
        self.label_25.setText(_translate("MainWindow", "Amplitud (Cos) (m)", None))
        self.label_24.setText(_translate("MainWindow", "Frecuencia (rad/s)", None))
        self.label_27.setText(_translate("MainWindow", "Exponente dec. (1/s)", None))
        self.label_31.setText(_translate("MainWindow", "Posicion de equilibrio (m)", None))
        self.Grupo_SolucionSobre.setTitle(_translate("MainWindow", "Solucion sobre amortiguada", None))
        self.label_22.setText(_translate("MainWindow", "Amplitud exp. 1 (m)", None))
        self.label_23.setText(_translate("MainWindow", "Exponente 1 (1/s)", None))
        self.label_28.setText(_translate("MainWindow", "Amplitud exp. 2 (m)", None))
        self.label_29.setText(_translate("MainWindow", "Exponente 2 (1/s)", None))
        self.label_32.setText(_translate("MainWindow", "Posicion de equilibrio (m)", None))
        self.label_30.setText(_translate("MainWindow", "En segundo grafico mostrar:", None))
        self.combo_grafico_secundario.setItemText(0, _translate("MainWindow", "Nada", None))
        self.control_animacion.setText(_translate("MainWindow", "Mostrar animacion", None))
        self.control_envolvente.setText(_translate("MainWindow", "Mostrar envolvente", None))
        self.Parametros.setTabText(self.Parametros.indexOf(self.ParametrosOscilatorio), _translate("MainWindow", "Problema Oscilatorio", None))
        self.V_OpcionesEscala.setTitle(_translate("MainWindow", "Opciones de escala", None))
        self.control_escalaautomatica.setText(_translate("MainWindow", "Escala vertical automatica", None))
        self.label_15.setText(_translate("MainWindow", "+/-", None))
        self.label_5.setText(_translate("MainWindow", "Escala vertical", None))
        self.label_13.setText(_translate("MainWindow", "x/t inicial", None))
        self.label_14.setText(_translate("MainWindow", "x/t final", None))
        self.label_3.setText(_translate("MainWindow", "Densidad (10^n)", None))
        self.Grupo_retenidos.setTitle(_translate("MainWindow", "Graficos almacenados", None))
        self.boton_agregar_acumulado.setText(_translate("MainWindow", "Agregar", None))
        self.boton_editar_acumulado.setText(_translate("MainWindow", "Editar", None))
        self.boton_quitar_acumulado.setText(_translate("MainWindow", "Quitar", None))
        self.boton_limpiar_acumulado.setText(_translate("MainWindow", "Limpiar", None))
        self.boton_acumulados_imagen.setText(_translate("MainWindow", "Guardar (imagen)", None))
        self.boton_acumulados_archivo.setText(_translate("MainWindow", "Guardar (csv)", None))
        self.Grupo_formula.setTitle(_translate("MainWindow", "Formula", None))
        self.etiqueta_formula.setText(_translate("MainWindow", "Aca va la formula", None))
        self.Grupo_graficos_animaciones.setTitle(_translate("MainWindow", "Graficos y animaciones", None))
        self.Grupo_animacion.setTitle(_translate("MainWindow", "Animacion", None))
        self.Grupo_graficos.setTitle(_translate("MainWindow", "Graficos", None))
        self.Grupo_grafico_principal.setTitle(_translate("MainWindow", "Principal", None))
        self.Grupo_grafico_secundario.setTitle(_translate("MainWindow", "Secundario", None))

