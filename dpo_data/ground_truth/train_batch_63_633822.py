import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.workplane(offset=-71/2).moveTo(-20,-78).cylinder(71,22).union(w0.sketch().push([(8.5,-16)]).rect(67,78).push([(-6,91)]).circle(9).push([(-6.5,85)]).rect(3,2,mode='s').push([(-1,91)]).circle(3,mode='s').finalize().extrude(-41))