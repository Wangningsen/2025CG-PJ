import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.workplane(offset=-122/2).moveTo(86,8.5).box(10,21,122).union(w0.sketch().arc((-55,13),(-39,-100),(3,6)).arc((-16,100),(-55,13)).assemble().push([(-20,49)]).circle(33,mode='s').finalize().extrude(-52))