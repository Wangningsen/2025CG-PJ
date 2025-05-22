import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-92,-41),(45,-41)).segment((45,-54)).segment((92,-54)).segment((92,54)).segment((45,54)).segment((45,39)).segment((-92,39)).close().assemble().finalize().extrude(-200)