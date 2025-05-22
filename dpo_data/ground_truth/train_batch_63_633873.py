import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.workplane(offset=-43/2).moveTo(79,43.5).box(42,3,43).union(w0.sketch().push([(-40,-42)]).rect(120,6).circle(2,mode='s').finalize().extrude(-9))