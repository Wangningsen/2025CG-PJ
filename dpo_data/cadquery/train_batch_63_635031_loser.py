import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,64,0))
w1=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((19,-93),(39,-100)).segment((78,17)).segment((58,24)).close().assemble().finalize().extrude(-128).union(w0.workplane(offset=-46/2).moveTo(-31.5,-56.5).box(93,33,46)).union(w0.sketch().segment((38,24),(42,24)).segment((42,37)).arc((76,58),(59,92)).segment((59,93)).segment((54,93)).arc((1,70),(38,24)).assemble().push([(30,54)]).circle(11,mode='s').finalize().extrude(-14)).union(w1.sketch().push([(9,58)]).rect(40,54).push([(1,79)]).rect(2,6,mode='s').finalize().extrude(29))