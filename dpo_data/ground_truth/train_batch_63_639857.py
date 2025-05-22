import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
w1=cq.Workplane('YZ',origin=(-37,0,0))
r=w0.workplane(offset=-19/2).moveTo(-69,-37).cylinder(19,31).union(w0.sketch().push([(75,43)]).circle(25).circle(22,mode='s').finalize().extrude(91)).union(w1.sketch().segment((-14,-3),(70,-3)).segment((70,11)).segment((8,11)).arc((8,9),(7,11)).segment((-14,11)).close().assemble().push([(28,3)]).circle(3,mode='s').finalize().extrude(75))