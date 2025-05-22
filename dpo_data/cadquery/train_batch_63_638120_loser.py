import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.workplane(offset=-38/2).moveTo(51,-24).box(98,78,38).union(w0.sketch().push([(-63,26)]).circle(37).push([(-65,1)]).circle(3,mode='s').finalize().extrude(110))