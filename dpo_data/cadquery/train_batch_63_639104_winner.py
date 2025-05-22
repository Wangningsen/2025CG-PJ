import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
w1=cq.Workplane('ZX',origin=(0,19,0))
r=w0.workplane(offset=-87/2).moveTo(-28,-88).cylinder(87,2).union(w0.workplane(offset=-37/2).moveTo(19,-4).cylinder(37,23)).union(w0.sketch().push([(-35,68)]).rect(46,44).reset().face(w0.sketch().segment((-20,15),(16,-47)).segment((58,-23)).segment((22,39)).close().assemble()).push([(19,-4)]).circle(10,mode='s').finalize().extrude(55)).union(w1.workplane(offset=-21/2).moveTo(-49,62).cylinder(21,38))