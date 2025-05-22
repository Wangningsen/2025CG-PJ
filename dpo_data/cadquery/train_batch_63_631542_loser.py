import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
r=w0.sketch().segment((-100,40),(-75,-15)).segment((-21,10)).segment((-21,-38)).segment((50,-38)).segment((50,26)).segment((-21,26)).segment((-21,16)).segment((-40,66)).close().assemble().finalize().extrude(3).union(w0.sketch().arc((39,-42),(89,-59),(85,-8)).segment((85,-42)).close().assemble().finalize().extrude(38))