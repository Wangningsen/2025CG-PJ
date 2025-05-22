import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.workplane(offset=-103/2).moveTo(8.5,29).box(59,32,103).union(w0.sketch().segment((-38,-45),(-30,-45)).segment((-30,-37)).segment((-35,-37)).arc((-36,-42),(-38,-45)).assemble().finalize().extrude(97))