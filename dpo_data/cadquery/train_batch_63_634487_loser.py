import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().push([(-46.5,0)]).rect(95,200).push([(-47,0)]).circle(19,mode='s').finalize().extrude(-76).union(w0.workplane(offset=-6/2).moveTo(63,-21).cylinder(6,31))