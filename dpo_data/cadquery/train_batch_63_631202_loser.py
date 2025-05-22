import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
w1=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.workplane(offset=-99/2).moveTo(28,49).cylinder(99,38).union(w0.sketch().push([(-28,-51)]).circle(36).push([(29,49)]).circle(15).finalize().extrude(101)).union(w1.sketch().segment((-38,-37),(5,-37)).segment((5,21)).arc((-40,78),(-38,7)).close().assemble().push([(-34,51)]).rect(2,2,mode='s').finalize().extrude(-57))