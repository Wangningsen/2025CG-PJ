import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.workplane(offset=-83/2).moveTo(-69.5,34.5).box(35,67,83).union(w0.sketch().segment((-24,-47),(22,-47)).segment((22,-68)).segment((41,-68)).segment((41,-47)).segment((87,-47)).segment((87,-15)).segment((41,-15)).segment((41,6)).segment((22,6)).segment((22,-15)).segment((-24,-15)).close().assemble().finalize().extrude(117))