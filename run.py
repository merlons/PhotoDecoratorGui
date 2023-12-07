"""
pip install PySide6==6.6.0 pyinstaller==6.1.0
PyInstaller -F -w --clean  -n PhotoDecorator ./run.py
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui.settings import CONFIG_FILE
from ui.tasks import WorkerThread
from ui.tools.config import MyConfig
from ui.tools.logger import LoggerThread
from ui.ui.MainWindow import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.config = MyConfig(CONFIG_FILE)  # 获取初始化参数
        self.init_kwargs()  # 初始化参数
        self.updateRunButtonState()  # 修改初始化状态
        self.logger_thread = LoggerThread()
        self.logger_thread.sig_logger.connect(self.signal_update_text_edit_logger)
        self.logger_thread.start()

    def init_ui(self):
        pass
        self.pushButton_input_dir.clicked.connect(self.handle_open_input_dir_dialog)
        self.pushButton_output_dir.clicked.connect(self.handle_open_output_dir_dialog)
        self.pushButton_run.clicked.connect(self.run)
        self.lineEdit_input_dir.textChanged.connect(self.updateRunButtonState)
        self.lineEdit_output_dir.textChanged.connect(self.updateRunButtonState)
        # self.actionFileOpenSourcePath.triggered.connect(self.handle_menu_file_open_source_path)
        # self.actionFileOpenTargetPath.triggered.connect(self.handle_menu_file_open_target_path)
        # self.actionOpenTempDir.triggered.connect(self.handle_menu_file_open_temp_dir)
        # self.actionClearTempDir.triggered.connect(self.handle_menu_file_clear_temp_dir)
        # self.actionSwitchLight.triggered.connect(self.handle_menu_theme_swich)
        # self.actionSwitchDark.triggered.connect(self.handle_menu_theme_swich)

    def init_kwargs(self):
        pass
        self.lineEdit_input_dir.setText(self.config.get('input_dir'))
        self.lineEdit_output_dir.setText(self.config.get('output_dir'))
        self.checkBox_shadow.setChecked(self.config.get('shadow', 0))
        self.checkBox_white_margin.setChecked(self.config.get('white_margin', 0))
        self.checkBox_use_equivalent_focal_length.setChecked(self.config.get('use_equivalent_focal_length', 0))
        self.checkBox_padding_with_original_ratio.setChecked(self.config.get('padding_with_original_ratio', 0))
        self.checkBox_logo_enable.setChecked(self.config.get('logo_enable', 0))

        self.comboBox_layout.setCurrentIndex(self.config.get('layout', 0))
        self.comboBox_left_top.setCurrentIndex(self.config.get('left_top', 0))
        self.comboBox_left_bottom.setCurrentIndex(self.config.get('left_bottom', 0))
        self.comboBox_right_top.setCurrentIndex(self.config.get('right_top', 0))
        self.comboBox_right_bottom.setCurrentIndex(self.config.get('right_bottom', 0))

        # theme.set(self.config.get('theme') if self.config.get('theme') else '明亮')

    def updateRunButtonState(self):
        # 如果两个文件夹都选择了，则启用运行按钮，否则禁用
        state = True if self.lineEdit_input_dir.text() and self.lineEdit_output_dir.text() else False
        self.pushButton_run.setEnabled(state)

    def signal_update_text_edit_logger(self, msg):
        self.textEdit_log.append(msg)

    def handle_open_input_dir_dialog(self):
        path = self.lineEdit_input_dir.text()
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹', '/' if not path else path)
        if folder_path:
            self.lineEdit_input_dir.setText(folder_path)
            self.updateRunButtonState()

    def handle_open_output_dir_dialog(self):
        path = self.lineEdit_output_dir.text()
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹', '/' if not path else path)
        if folder_path:
            self.lineEdit_output_dir.setText(folder_path)
            self.updateRunButtonState()

    def get_current_value(self):
        kwargs = {
            "input_dir": self.lineEdit_input_dir.text(),
            "output_dir": self.lineEdit_output_dir.text(),

            "shadow": self.checkBox_shadow.checkState().value,
            "white_margin": self.checkBox_white_margin.checkState().value,
            "use_equivalent_focal_length": self.checkBox_use_equivalent_focal_length.checkState().value,
            "padding_with_original_ratio": self.checkBox_padding_with_original_ratio.checkState().value,
            "logo_enable": self.checkBox_logo_enable.checkState().value,

            "layout": self.comboBox_layout.currentIndex(),
            "left_top": self.comboBox_left_top.currentIndex(),
            "left_bottom": self.comboBox_left_bottom.currentIndex(),
            "right_bottom": self.comboBox_right_bottom.currentIndex(),
            "right_top": self.comboBox_right_top.currentIndex(),
        }
        self.config.update(kwargs)
        return kwargs

    def run(self):
        kwargs = self.get_current_value()
        self.worker_thread = WorkerThread(**kwargs)
        self.worker_thread.finished.connect(self.run_finished)
        self.worker_thread.start()
        self.pushButton_run.setEnabled(False)  # 防止多次点击运行按钮

    def run_finished(self):
        QMessageBox.information(self, '运行完成', '后台处理完成！')
        self.pushButton_run.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
