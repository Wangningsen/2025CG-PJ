import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,26))
w1=cq.Workplane('ZX',origin=(0,-14,0))
r=w0.sketch().push([(38,18)]).circle(17).circle(10,mode='s').finalize().extrude(-126).union(w0.workplane(offset=-104/2).moveTo(-68,33).box(28,108,104)).union(w0.sketch().arc((-6,16),(38,9),(82,19)).segment((-4,19)).arc((-5,17),(-6,16)).assemble().finalize().extrude(28)).union(w1.sketch().segment((8,27),(11,27)).arc((54,-6),(97,27)).segment((100,27)).segment((100,49)).segment((97,49)).arc((54,81),(11,49)).segment((8,49)).close().assemble().finalize().extrude(-73))