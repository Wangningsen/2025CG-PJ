import cadquery as cq
w0=cq.Workplane('YZ',origin=(-75,0,0))
w1=cq.Workplane('ZX',origin=(0,57,0))
r=w0.workplane(offset=41/2).moveTo(48,-75).box(38,30,41).union(w1.sketch().segment((-90,-56),(-87,-56)).arc((-75,-100),(-63,-56)).segment((-12,-56)).arc((5,-58),(21,-56)).segment((69,-56)).arc((66,-23),(99,-14)).segment((99,98)).segment((21,98)).arc((5,100),(-12,98)).segment((-90,98)).close().assemble().finalize().extrude(-124))