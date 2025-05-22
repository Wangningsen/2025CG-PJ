import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,77,0))
w1=cq.Workplane('ZX',origin=(0,78,0))
r=w0.sketch().segment((-100,-61),(-97,-65)).segment((-89,-60)).segment((-91,-57)).close().assemble().finalize().extrude(-154).union(w0.workplane(offset=-70/2).moveTo(34,0).cylinder(70,66)).union(w1.sketch().segment((-79,-54),(13,-54)).segment((13,-46)).segment((-79,-46)).segment((-79,-47)).arc((-77,-48),(-79,-49)).close().assemble().finalize().extrude(-71))