import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Konversi Mata Uang')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.usd_label = QLabel('USD:')
        layout.addWidget(self.usd_label)

        self.usd_line = QLineEdit()
        layout.addWidget(self.usd_line)

        self.convert_button = QPushButton('Convert')
        layout.addWidget(self.convert_button)

        self.eur_label = QLabel('EUR:')
        layout.addWidget(self.eur_label)

        self.eur_line = QLineEdit()
        self.eur_line.setReadOnly(True)
        layout.addWidget(self.eur_line)

        self.gbp_label = QLabel('GBP:')
        layout.addWidget(self.gbp_label)

        self.gbp_line = QLineEdit()
        self.gbp_line.setReadOnly(True)
        layout.addWidget(self.gbp_line)

        self.jpy_label = QLabel('JPY:')
        layout.addWidget(self.jpy_label)

        self.jpy_line = QLineEdit()
        self.jpy_line.setReadOnly(True)
        layout.addWidget(self.jpy_line)

        self.convert_button.clicked.connect(self.convert_currency)

    def convert_currency(self):
        try:
            usd_amount = float(self.usd_line.text())
            eur_amount = usd_amount * 0.85  # Kurs EUR-USD: 0.85
            gbp_amount = usd_amount * 0.75  # Kurs GBP-USD: 0.75
            jpy_amount = usd_amount * 110.23  # Kurs JPY-USD: 110.23

            self.eur_line.setText(str(eur_amount))
            self.gbp_line.setText(str(gbp_amount))
            self.jpy_line.setText(str(jpy_amount))
        except ValueError:
            self.eur_line.setText('')
            self.gbp_line.setText('')
            self.jpy_line.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())
