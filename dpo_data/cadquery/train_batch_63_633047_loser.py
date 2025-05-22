import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.workplane(offset=-122/2).moveTo(86,8.5).box(10,21,122).union(w0.sketch().arc((-52,14),(-37,-100),(-1,9)).arc((-17,100),(-52,14)).assemble().push([(-20,49)]).circle(32,mode='s').finalize().extrude(-52))