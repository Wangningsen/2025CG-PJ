import cadquery as cq
w0=cq.Workplane('YZ',origin=(2,0,0))
r=w0.workplane(offset=-48/2).moveTo(-14,0).box(12,200,48).union(w0.sketch().segment((-1,-41),(20,-70)).arc((13,-51),(-1,-41)).assemble().finalize().extrude(44))