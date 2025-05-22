import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-84,0))
w1=cq.Workplane('YZ',origin=(-92,0,0))
r=w0.workplane(offset=184/2).moveTo(0,-28).cylinder(184,33).union(w1.sketch().push([(-23,0)]).rect(154,52).push([(-23,-0.5)]).rect(44,27,mode='s').finalize().extrude(184))