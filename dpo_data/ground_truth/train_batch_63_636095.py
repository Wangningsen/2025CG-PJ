import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.workplane(offset=-160/2).moveTo(-53,13).cylinder(160,47).union(w0.sketch().segment((58,-60),(100,-60)).arc((79,-52),(58,-60)).assemble().finalize().extrude(-19))