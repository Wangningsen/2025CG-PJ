import cadquery as cq
w0=cq.Workplane('YZ',origin=(2,0,0))
r=w0.workplane(offset=-48/2).moveTo(-14,0).box(12,200,48).union(w0.sketch().arc((-1,-41),(12,-59),(20,-70)).arc((14,-52),(-1,-41)).assemble().finalize().extrude(44))