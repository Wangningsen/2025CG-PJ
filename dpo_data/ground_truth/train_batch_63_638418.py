import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-45))
r=w0.workplane(offset=46/2).moveTo(-87,67).cylinder(46,13).union(w0.sketch().push([(83,-63)]).circle(17).circle(11,mode='s').finalize().extrude(91))