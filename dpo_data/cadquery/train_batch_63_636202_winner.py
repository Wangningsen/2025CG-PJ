import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().arc((-76,65),(65,-76),(-41,91)).segment((-41,67)).segment((-73,67)).arc((-75,66),(-76,65)).assemble().push([(2,1)]).circle(56,mode='s').finalize().extrude(45)