import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,39,0))
r=w0.sketch().segment((76,-63),(100,-63)).segment((100,-42)).segment((92,-42)).segment((87,-50)).segment((81,-53)).segment((80,-54)).segment((76,-56)).close().assemble().finalize().extrude(-78).union(w0.workplane(offset=-75/2).moveTo(-80,43).cylinder(75,20))