import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
w1=cq.Workplane('XY',origin=(0,0,-40))
r=w0.sketch().circle(83).circle(55,mode='s').finalize().extrude(141).union(w0.sketch().circle(65).reset().face(w0.sketch().segment((-10,-54),(10,-54)).segment((10,-48)).arc((52,0),(10,48)).segment((10,54)).segment((-10,54)).segment((-10,48)).arc((-52,0),(-10,-48)).close().assemble(),mode='s').finalize().extrude(144)).union(w1.workplane(offset=15/2).moveTo(-57,-2).cylinder(15,43))