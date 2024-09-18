#ch 5.2.1 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage) #버튼 클릭 시 핸들러 함수 연결
        self.view.btn2.clicked.connect(self.view.clearMessage) #버튼 2 핸들러 함수 연결