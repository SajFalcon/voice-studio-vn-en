import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QComboBox, QFileDialog, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QPlainTextEdit,
    QProgressBar, QVBoxLayout, QWidget
)


class VoiceStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Studio VN-EN")
        self.resize(900, 680)
        self.reference_audio = ""

        central = QWidget()
        self.setCentralWidget(central)
        outer = QVBoxLayout(central)
        outer.setContentsMargins(24, 22, 24, 22)
        outer.setSpacing(14)

        title = QLabel("Voice Studio <span style='color:#3b82f6'>VN-EN</span>")
        title.setTextFormat(Qt.TextFormat.RichText)
        title.setStyleSheet("font-size: 27px; font-weight: 700;")
        subtitle = QLabel("Voice cloning workspace · Vietnamese & English")
        subtitle.setStyleSheet("color: #7b8494; font-size: 13px;")
        outer.addWidget(title)
        outer.addWidget(subtitle)

        card = QFrame()
        card.setObjectName("card")
        form = QFormLayout(card)
        form.setContentsMargins(18, 18, 18, 18)
        form.setVerticalSpacing(14)
        form.setHorizontalSpacing(18)

        self.mode = QComboBox()
        self.mode.addItems(["Offline model (local inference)", "Online provider (API)"])
        form.addRow("Processing mode", self.mode)

        self.language = QComboBox()
        self.language.addItems(["Vietnamese", "English"])
        form.addRow("Output language", self.language)

        audio_row = QWidget()
        audio_layout = QHBoxLayout(audio_row)
        audio_layout.setContentsMargins(0, 0, 0, 0)
        self.audio_path = QLineEdit()
        self.audio_path.setPlaceholderText("Select a reference recording (WAV/MP3)")
        self.audio_path.setReadOnly(True)
        browse = QPushButton("Browse…")
        browse.clicked.connect(self.choose_audio)
        audio_layout.addWidget(self.audio_path, 1)
        audio_layout.addWidget(browse)
        form.addRow("Reference voice", audio_row)

        self.text = QPlainTextEdit()
        self.text.setPlaceholderText("Enter the text you want to synthesize…")
        self.text.setMinimumHeight(190)
        form.addRow("Text to speak", self.text)
        outer.addWidget(card)

        note = QLabel(
            "Prototype status: the desktop interface and Windows build pipeline are ready. "
            "The voice inference adapter has not been connected to a model or online API yet."
        )
        note.setWordWrap(True)
        note.setStyleSheet(
            "padding: 12px; border-radius: 8px; background: #fff4d6; color: #674d00;"
        )
        outer.addWidget(note)

        buttons = QHBoxLayout()
        self.status = QLabel("Ready")
        self.status.setStyleSheet("color: #7b8494;")
        buttons.addWidget(self.status, 1)
        self.generate = QPushButton("Generate speech")
        self.generate.setMinimumHeight(40)
        self.generate.clicked.connect(self.generate_speech)
        buttons.addWidget(self.generate)
        outer.addLayout(buttons)

        self.progress = QProgressBar()
        self.progress.setRange(0, 1)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(5)
        outer.addWidget(self.progress)

        self.setStyleSheet("""
            QMainWindow { background: #f4f6fa; }
            QFrame#card { background: white; border: 1px solid #e0e5ed; border-radius: 12px; }
            QLabel { color: #202938; }
            QLineEdit, QPlainTextEdit, QComboBox {
                background: white; border: 1px solid #d4dae4; border-radius: 7px;
                padding: 9px; color: #202938; font-size: 13px;
            }
            QPushButton {
                background: #2563eb; color: white; border: none; border-radius: 7px;
                padding: 10px 16px; font-weight: 600;
            }
            QPushButton:hover { background: #1d4ed8; }
        """)

    def choose_audio(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Choose reference audio", "",
            "Audio files (*.wav *.mp3 *.flac *.m4a);;All files (*.*)"
        )
        if path:
            self.reference_audio = path
            self.audio_path.setText(path)

    def generate_speech(self):
        if not self.text.toPlainText().strip():
            QMessageBox.information(self, "Text required", "Enter the text you want to synthesize.")
            return
        QMessageBox.information(
            self,
            "Model not connected yet",
            "The GUI is a starter scaffold. The next development step is to connect and test "
            "a licensed Vietnamese/English voice model or an online API provider. No audio "
            "has been generated."
        )


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Voice Studio VN-EN")
    window = VoiceStudio()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
