import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
w1=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.workplane(offset=-54/2).moveTo(-77.5,79).box(19,24,54).union(w0.sketch().segment((-26,-58),(8,-90)).segment((87,-9)).segment((54,23)).close().assemble().push([(5,-60)]).circle(7,mode='s').finalize().extrude(115)).union(w1.sketch().arc((-79,-8),(-52,18),(-25,-6)).arc((-16,57),(-75,71)).segment((-75,72)).arc((-100,31),(-79,-8)).assemble().finalize().extrude(-56))