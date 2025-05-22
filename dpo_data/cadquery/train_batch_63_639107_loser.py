import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
w1=cq.Workplane('YZ',origin=(25,0,0))
r=w0.workplane(offset=-87/2).moveTo(-15,32).cylinder(87,47).union(w1.sketch().segment((57,-79),(57,-76)).segment((62,-76)).arc((59,-71),(58,-67)).arc((58,-68),(57,-69)).segment((57,-67)).arc((55,-73),(57,-79)).assemble().finalize().extrude(75))