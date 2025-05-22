import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.workplane(offset=-98/2).moveTo(-65.5,85).box(21,30,98).union(w0.sketch().arc((47,-76),(46,-89),(51,-100)).segment((63,-100)).segment((63,-61)).arc((-25,22),(47,-76)).assemble().finalize().extrude(64))