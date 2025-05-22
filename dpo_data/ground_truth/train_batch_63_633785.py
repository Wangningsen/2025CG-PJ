import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=195/2).box(108,174,195).union(w0.sketch().segment((-48,-34),(-7,-34)).segment((-37,10)).segment((0,34)).segment((-48,34)).close().assemble().finalize().extrude(200))