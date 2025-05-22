import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
r=w0.sketch().segment((-100,40),(-77,-15)).segment((-21,8)).segment((-21,-38)).segment((50,-38)).segment((50,26)).segment((-21,26)).segment((-21,18)).segment((-39,66)).close().assemble().finalize().extrude(3).union(w0.sketch().arc((39,-42),(91,-57),(85,-8)).segment((85,-42)).close().assemble().finalize().extrude(38))