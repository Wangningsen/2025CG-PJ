import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().arc((-17,85),(-76,-41),(63,-60)).segment((53,-60)).segment((53,-15)).segment((87,-15)).close().assemble().finalize().extrude(-110).union(w0.workplane(offset=-75/2).moveTo(-21,41).cylinder(75,44)).union(w0.workplane(offset=90/2).moveTo(1,1).cylinder(90,45))