import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-66,-23),(66,-23)).arc((-1,23),(-66,-23)).assemble().finalize().extrude(-200)