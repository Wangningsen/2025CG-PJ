import cadquery as cq
w0=cq.Workplane('YZ',origin=(25,0,0))
w1=cq.Workplane('YZ',origin=(25,0,0))
r=w0.sketch().arc((-57,-15),(64,-74),(31,55)).arc((-67,86),(-57,-15)).assemble().finalize().extrude(-50).union(w1.workplane(offset=-49/2).moveTo(17,-50.5).box(12,99,49))