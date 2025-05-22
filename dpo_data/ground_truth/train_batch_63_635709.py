import cadquery as cq
w0=cq.Workplane('YZ',origin=(-26,0,0))
r=w0.sketch().arc((-71,-7),(-69,-3),(-66,2)).segment((-24,2)).segment((-24,25)).arc((-23,27),(-21,29)).arc((1,26),(20,15)).arc((6,84),(-65,92)).segment((-71,92)).segment((-71,87)).arc((-94,40),(-71,-7)).assemble().push([(22,40)]).circle(3,mode='s').finalize().extrude(-17).union(w0.workplane(offset=70/2).moveTo(39,-45).cylinder(70,55))