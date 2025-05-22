import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
w1=cq.Workplane('YZ',origin=(-37,0,0))
r=w0.workplane(offset=-19/2).moveTo(-69,-37).cylinder(19,31).union(w0.sketch().push([(75,43)]).circle(25).circle(22,mode='s').finalize().extrude(91)).union(w1.sketch().segment((-14,-3),(22,-3)).segment((22,-2)).segment((23,-2)).segment((23,-3)).segment((70,-3)).segment((70,11)).segment((-14,11)).close().assemble().push([(28,1)]).rect(6,2,mode='s').finalize().extrude(75))