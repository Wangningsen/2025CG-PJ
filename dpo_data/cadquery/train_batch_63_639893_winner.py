import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().segment((7,-94),(8,-100)).segment((71,-90)).segment((70,-85)).close().assemble().finalize().extrude(-40).union(w0.workplane(offset=-5/2).moveTo(-63,63).box(16,74,5)).union(w0.workplane(offset=-1/2).moveTo(-22,-14).box(46,46,1))