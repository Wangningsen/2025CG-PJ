import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().segment((85,76),(85,79)).segment((92,79)).segment((92,72)).segment((89,72)).arc((97,73),(100,81)).segment((99,81)).segment((95,81)).segment((95,86)).segment((96,86)).arc((87,85),(85,76)).assemble().finalize().extrude(-27).union(w0.workplane(offset=3/2).moveTo(-59,-60.5).box(82,53,3))