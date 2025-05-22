import cadquery as cq
w0=cq.Workplane('YZ',origin=(-76,0,0))
r=w0.workplane(offset=104/2).moveTo(95.5,25.5).box(9,59,104).union(w0.sketch().push([(-16,-49.5)]).rect(168,11).push([(-24.5,-46.5)]).rect(3,1,mode='s').finalize().extrude(152))