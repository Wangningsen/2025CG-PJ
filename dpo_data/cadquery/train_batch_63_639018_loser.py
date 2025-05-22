import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
w1=cq.Workplane('XY',origin=(0,0,13))
r=w0.workplane(offset=-100/2).moveTo(-55,4).cylinder(100,45).union(w0.sketch().push([(94,-70)]).circle(6).push([(94,-69.5)]).rect(2,9,mode='s').finalize().extrude(-77)).union(w1.sketch().arc((-21,54),(28,9),(28,76)).arc((25,25),(-21,54)).assemble().finalize().extrude(-48))