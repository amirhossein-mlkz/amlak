from uiFiles.main_UI import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6 import QtGui

class Styler:

    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui

        self.shadows_obj: dict[QtWidgets.QWidget] = {
            'menu':
                {   
                    'style': {'blur_radius':10,
                              'offset':(0,0),
                              'color':(0,0,0,50),
                              },
                    'objects':[ self.ui.all_rent_building,
                                self.ui.all_sale_building,
                                self.ui.profile,
                                self.ui.register_rent_building,
                                self.ui.register_sale_building,
                                self.ui.users,
                                ]
                },



        }

        # self.layout_obj: dict[QtWidgets.QWidget] = {
        #     'message': 
        #         {   
        #             'style': {'layout_type': 'vertical',
        #                       'spacer_type': 'vertical'
        #                       },
        #             'objects':[ self.ui.register_message_frame,
        #                         self.ui.change_username_message_frame,
        #                         self.ui.change_password_message_frame
        #                         ]
        #         },
        # } 

    def render(self,):

        self.__set_shadow()
        #self.__set_layout()
        self.all_style_repoblish()
        
    
    def all_style_repoblish(self,):
        #for widget in self.ui.
        for atr_name in dir(self.ui):
            atr = getattr(self.ui, atr_name)
            try:
                atr.style().unpolish(atr)
                atr.style().polish(atr)
            except:
                pass

    def __set_shadow(self, ):
        for group_name, group in self.shadows_obj.items():
            style = group['style']
            objects:list[QtWidgets.QWidget] = group['objects']
            for obj in objects:
                shadow  = QtWidgets.QGraphicsDropShadowEffect(obj)
                shadow.setBlurRadius(style['blur_radius'])
                shadow.setOffset(*style['offset'])
                shadow.setColor(QtGui.QColor(*style['color']))
                obj.setGraphicsEffect(shadow)

    
    def __set_hover_scale(self,):
        pass
    

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            print("Mouse is over the label")
            self.stop = True
            print('program stop is', self.stop)
            return True
        elif event.type() == QEvent.Leave:
            print("Mouse is not over the label")
            self.stop = False
            print('program stop is', self.stop)
        return False

    # def __set_layout(self, ):
    #     for group_name, group in self.layout_obj.items():
    #         style = group['style']
    #         objects:list[QtWidgets.QWidget] = group['objects']
    #         for obj in objects:
    #             layout = QtWidgets.QHBoxLayout() if style['layout_type']=='horizontal' else QtWidgets.QVBoxLayout()
    #             spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum) if style['layout_type']=='horizontal' \
    #                 else QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
    #             obj.setLayout(layout)
    #             layout.addItem(spacer)
