import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.workplane(offset=-71/2).moveTo(-20,-78).cylinder(71,22).union(w0.sketch().push([(8.5,-16)]).rect(67,78).push([(-6,91)]).circle(9).push([(-5.5,91)]).rect(3,10,mode='s').finalize().extrude(-40))