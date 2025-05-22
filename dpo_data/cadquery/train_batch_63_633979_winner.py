import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().push([(46,57)]).circle(32).circle(28,mode='s').finalize().extrude(-105).union(w0.workplane(offset=25/2).moveTo(-28.5,34).box(33,36,25)).union(w0.workplane(offset=95/2).moveTo(-37,-72).box(82,34,95))