import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
w1=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.workplane(offset=-15/2).moveTo(-91,70).cylinder(15,9).union(w0.sketch().push([(14,-34)]).circle(45).circle(43,mode='s').finalize().extrude(132)).union(w1.workplane(offset=101/2).moveTo(-34,-66.5).box(46,35,101))