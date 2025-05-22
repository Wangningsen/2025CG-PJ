import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
w1=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.workplane(offset=-54/2).moveTo(-77.5,79).box(19,24,54).union(w0.sketch().segment((-26,-58),(7,-91)).segment((87,-9)).segment((54,23)).segment((4,-34)).segment((-1,-33)).close().assemble().push([(5,-61)]).circle(7,mode='s').finalize().extrude(115)).union(w1.sketch().arc((-80,-7),(-51,19),(-27,-7)).arc((-14,1),(-5,14)).segment((4,14)).segment((4,51)).segment((-5,51)).arc((-23,64),(-43,55)).arc((-46,76),(-63,75)).arc((-99,40),(-80,-7)).assemble().finalize().extrude(-56))