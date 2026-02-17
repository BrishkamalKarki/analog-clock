from PySide6.QtGui import QPen
from PySide6.QtCore import Qt

def get_pens():

    # This includes the pen defination
    # All the Enums should in aranged order as the QPen method is strict
    pens={
            'tick_normal':QPen(Qt.gray, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'tick_hour':QPen(Qt.gray, 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'text':QPen(Qt.lightGray,1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'inner_center':QPen(Qt.white, 6, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'outer_center':QPen(Qt.black, 7, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'date_box': QPen(Qt.green, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'date_text': QPen(Qt.green, 4, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'hour_hand': QPen(Qt.white, 5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'min_hand': QPen(Qt.white, 3.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
            'sec_hand': QPen(Qt.red, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        }

    return pens