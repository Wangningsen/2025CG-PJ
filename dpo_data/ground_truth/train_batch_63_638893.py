import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().arc((28,6),(9,-4),(30,2)).arc((25,3),(28,6)).assemble().finalize().extrude(-114).union(w0.sketch().segment((-42,-16),(15,-16)).segment((30,-21)).segment((32,-16)).segment((42,-16)).segment((42,42)).segment((-42,42)).close().assemble().finalize().extrude(-5)).union(w0.workplane(offset=86/2).moveTo(19,0).box(40,118,86))