import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().rect(174,76).reset().face(w0.sketch().segment((-26,20),(-21,13)).arc((-18,-14),(9,-21)).segment((14,-28)).segment((26,-20)).segment((21,-13)).arc((18,14),(-9,21)).segment((-14,28)).close().assemble(),mode='s').finalize().extrude(200)