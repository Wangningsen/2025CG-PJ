import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
w1=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.workplane(offset=-99/2).moveTo(29,49).cylinder(99,38).union(w0.workplane(offset=20/2).moveTo(29,49).cylinder(20,9)).union(w0.sketch().push([(-28,-51)]).circle(36).push([(29,49)]).circle(15).finalize().extrude(101)).union(w1.sketch().segment((-38,-37),(-19,-37)).segment((-19,-45)).segment((-14,-45)).segment((-14,-37)).segment((5,-37)).segment((5,30)).arc((-46,76),(-38,7)).close().assemble().finalize().extrude(-57))