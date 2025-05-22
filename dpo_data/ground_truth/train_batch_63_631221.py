import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
r=w0.sketch().segment((-51,-91),(-48,-93)).segment((-46,-89)).arc((88,-48),(49,87)).segment((51,91)).segment((48,93)).segment((46,89)).arc((-88,48),(-49,-87)).close().assemble().circle(19,mode='s').finalize().extrude(-92)