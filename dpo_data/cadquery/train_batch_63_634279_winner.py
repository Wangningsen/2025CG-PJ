import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().arc((-17,42),(-98,-14),(0,-31)).arc((12,-20),(16,-5)).arc((15,29),(-15,40)).arc((-16,39),(-17,42)).assemble().reset().face(w0.sketch().arc((-17,41),(-97,-13),(-1,-28)).arc((-31,4),(-17,41)).assemble(),mode='s').reset().face(w0.sketch().arc((88,40),(99,39),(91,46)).arc((89,43),(88,40)).assemble()).finalize().extrude(-57)