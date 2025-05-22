import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
w1=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.workplane(offset=-45/2).moveTo(59,-59).cylinder(45,41).union(w0.sketch().push([(-86,-20)]).circle(14).push([(-86.5,-20)]).rect(25,6,mode='s').finalize().extrude(110)).union(w1.workplane(offset=49/2).moveTo(23,61.5).box(40,77,49))