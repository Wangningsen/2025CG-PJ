import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,45))
r=w0.sketch().arc((-46,56),(-33,-47),(34,28)).segment((34,100)).segment((-46,100)).close().assemble().finalize().extrude(-90).union(w0.sketch().arc((70,-100),(74,-93),(70,-86)).close().assemble().finalize().extrude(-88))