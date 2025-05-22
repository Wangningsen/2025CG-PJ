import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().push([(20,70)]).circle(14).push([(15,63)]).circle(3,mode='s').finalize().extrude(-98).union(w0.workplane(offset=102/2).moveTo(0,-34.5).box(70,97,102))