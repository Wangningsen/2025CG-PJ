import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().arc((24,-51),(100,-19),(28,22)).segment((46,19)).segment((42,-9)).segment((24,-6)).arc((-100,-26),(24,-51)).assemble().finalize().extrude(-46).union(w1.sketch().segment((-4,-65),(9,-65)).segment((9,-63)).arc((25,-42),(9,-21)).segment((9,-19)).segment((-4,-19)).segment((-4,-21)).arc((-19,-42),(-4,-63)).close().assemble().finalize().extrude(111))