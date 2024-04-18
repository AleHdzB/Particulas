from PySide2.QtWidgets import QMainWindow,QFileDialog, QMessageBox,QTableWidgetItem, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from admin_particulas import Admin

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.admin = Admin()

        self.ui.pushButton_agregar_inicio.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton_agregar_final.clicked.connect(self.click_agregar_final)
        self.ui.pushButton_mostrar.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

    @Slot()
    def buscar_id(self):
       # print("Buscar ID")
        id = self.ui.Buscar_lineEdit.text()

        encontrado = False
        for particula in self.admin:
            if int(id) == particula.id:
                self.ui.tabla.clear() #Limpiar tabla
                self.ui.tabla.setColumnCount(10) #Config. numero de columnas
                headers = ["ID","ORIGEN_X","ORIGEN_Y","DESTINO_X","DESTINO_Y","VELOCIDAD","RED",
                        "BLUE","GREEN","DISTANCIA"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)  #Headers de Columnas
                self.ui.tabla.setRowCount(1)#Config Filas
                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))   
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                blue_widget = QTableWidgetItem(str(particula.blue))
                green_widget = QTableWidgetItem(str(particula.green))
                distancia_widget = QTableWidgetItem(str(particula.distancia))    

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, blue_widget)
                self.ui.tabla.setItem(0, 8, green_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el identificador "(id)" no fue encontrado'
            )


    @Slot()
    def mostrar_tabla(self):
        #print('Mostrar tabla')
        self.ui.tabla.setColumnCount(10) #Config. numero de columnas
        headers = ["ID","ORIGEN_X","ORIGEN_Y","DESTINO_X","DESTINO_Y","VELOCIDAD","RED",
                   "BLUE","GREEN","DISTANCIA"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)  #Headers de Columnas

        self.ui.tabla.setRowCount(len(self.admin)) #Config. numero de Filas

        row = 0
        for particula in self.admin:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))   
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            blue_widget = QTableWidgetItem(str(particula.blue))
            green_widget = QTableWidgetItem(str(particula.green))
            distancia_widget = QTableWidgetItem(str(particula.distancia))    

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, blue_widget)
            self.ui.tabla.setItem(row, 8, green_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1
    @Slot()
    def action_Abrir_Archivo(self):
        #print("Abrir_Archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'   
        )[0]
        print(ubicacion)
        if self.admin.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo ABRIR el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "NO se pudo ABRIR el archivo " + ubicacion
            )

    @Slot()
    def action_Guardar_Archivo(self):
        print("Guardar_Archivo")
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON(*.json)'
        )[0]
        print(ubicacion)
        if self.admin.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "NO se pudo crear el archivo" + ubicacion
            )
      
    
    @Slot()
    def click_agregar_inicio(self):
        origen_x = self.ui.spinBox_origen_x.value()
        origen_y = self.ui.spinBox_origen_y.value()
        destino_x = self.ui.spinBox_destino_x.value()
        destino_y = self.ui.spinBox_destino_y.value()
        velocidad = self.ui.spinBox_velocidad.value()
        red = self.ui.spinBox_red.value()
        green = self.ui.spinBox_green.value()
        blue = self.ui.spinBox_blue.value()

        particula = Particula(origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregar_inicio(particula)        
           
    @Slot()
    def click_agregar_final(self):
        origen_x = self.ui.spinBox_origen_x.value()
        origen_y = self.ui.spinBox_origen_y.value()
        destino_x = self.ui.spinBox_destino_x.value()
        destino_y = self.ui.spinBox_destino_y.value()
        velocidad = self.ui.spinBox_velocidad.value()
        red = self.ui.spinBox_red.value()
        green = self.ui.spinBox_green.value()
        blue = self.ui.spinBox_blue.value()

        particula = Particula(origen_x, origen_y,destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregar_final(particula)   
        
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.admin))

    