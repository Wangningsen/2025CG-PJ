import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-92,0))
w1=cq.Workplane('YZ',origin=(-92,0,0))
r=w0.workplane(offset=184/2).moveTo(0,-74).cylinder(184,26).union(w1.sketch().push([(-75,0)]).circle(7).push([(-75.5,0)]).rect(11,6,mode='s').finalize().extrude(192))