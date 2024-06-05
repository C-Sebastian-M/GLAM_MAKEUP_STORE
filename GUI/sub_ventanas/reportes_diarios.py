from typing import List, Union

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QTableWidget,
    QHeaderView, QGraphicsDropShadowEffect,
    QFileDialog
)
from PyQt5.QtGui import ( QColor, QTextDocument )
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

from GUI.sub_ventanas.custom.utils.css import CBackground

class ReportesDiarios(QWidget, CBackground):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportesDiarios\reportesDiarios.ui", 
            self
        )

class Plantilla(QWidget):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__()
        uic.loadUi(
            r"GUI\sub_ventanas\ui\reportesDiarios\reportesDiariosPlantilla.ui", 
            self
        )

        self.title: str = title
        self.campos: List[Union[str, int, float]]  = columns

        self.__inicializar__()
        self.imprimirBtn.clicked.connect(self.__imprimir__)
        self.pdfBtn.clicked.connect(self.__PDF__)
        self.pintar()

    def __inicializar__(self) -> None:
        self.rDPlantillaTitle.setText(self.title)
        self.__inicializar_tabla__()

    def __inicializar_tabla__(self) -> None:
        table: QTableWidget = self.tableReporteDiario
        table.setColumnCount(len(self.campos))
        table.setHorizontalHeaderLabels(self.campos)
        table.resizeColumnsToContents()
        table.verticalHeader().setDefaultSectionSize(20)

        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(8)
        shadow_effect.setColor(QColor(0, 0, 0, 70))
        shadow_effect.setOffset(0, 0)
        header.setGraphicsEffect(shadow_effect)

        table.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def __imprimir__(self) -> None:
        printer = QPrinter()

        dialogo = QPrintDialog(printer, self)
        if dialogo.exec_() == QPrintDialog.Accepted:
            document = QTextDocument()

            html = self.__to_html__()

            document.setHtml(html)

            document.print_(printer)

    def __to_html__(self):
        html = "<html><head></head><body><table border='1'>"

        # Añadir campos
        html += "<tr>"
        for column in range(self.tableReporteDiario.columnCount()):
            header = self.tableReporteDiario.horizontalHeaderItem(column)
            html += f"<th>{header.text()}</th>"
        html += "</tr>"

        # Añadir registros
        for row in range(self.tableReporteDiario.rowCount()):
            html += "<tr>"
            for column in range(self.tableReporteDiario.columnCount()):
                item = self.tableReporteDiario.item(row, column)
                html += f"<td>{item.text() if item else ''}</td>"
            html += "</tr>"

        html += "</table></body></html>"
        return html
    
    def __PDF__(self) -> None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save as PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if file_path:
            printer = QPrinter(QPrinter.PdfFormat)
            printer.setOutputFileName(file_path)

            document = QTextDocument()

            html = self.table_widget_to_html()

            document.setHtml(html)

            document.print_(printer)

    def pintar(self) -> None:
        with open(r"GUI\sub_ventanas\css\reportes_diarios.css", "r") as style_file:
            style_line = style_file.read()

        self.setStyleSheet(style_line)
        style_file.close()

class ReporteDiarioVentas(Plantilla):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__(title, columns)

class ReporteDiarioProductos(Plantilla):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__(title, columns)

class ReporteDiarioCatalogo(Plantilla):
    def __init__(self, title: str, columns: List[str]) -> None:
        super().__init__(title, columns)
