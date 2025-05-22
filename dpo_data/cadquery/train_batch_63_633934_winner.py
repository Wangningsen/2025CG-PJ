import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,36,0))
w1=cq.Workplane('YZ',origin=(4,0,0))
r=w0.sketch().arc((-1,46),(-96,-32),(27,-32)).arc((97,38),(-1,46)).assemble().reset().face(w0.sketch().arc((6,38),(23,17),(28,-9)).segment((81,-8)).segment((79,46)).segment((6,45)).close().assemble(),mode='s').finalize().extrude(-126).union(w0.workplane(offset=-111/2).moveTo(44,19).cylinder(111,35)).union(w1.sketch().segment((56,4),(90,4)).segment((90,48)).segment((90,53)).segment((56,53)).segment((56,48)).close().assemble().finalize().extrude(-60))