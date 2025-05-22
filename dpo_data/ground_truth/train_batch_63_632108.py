import cadquery as cq
w0=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-53,-100),(30,-100)).segment((7,-37)).segment((28,-29)).segment((-53,-29)).close().assemble().push([(-42,-98)]).circle(1,mode='s').finalize().extrude(-32).union(w0.workplane(offset=47/2).moveTo(12,59).cylinder(47,41))