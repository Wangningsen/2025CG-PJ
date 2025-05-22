import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-53,0))
w1=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-70,-92),(46,-92)).segment((46,-66)).arc((76,0),(46,66)).segment((46,92)).segment((-70,92)).segment((-70,66)).arc((-100,0),(-70,-66)).close().assemble().finalize().extrude(106).union(w1.sketch().segment((-63,-43),(-60,-43)).segment((-60,-42)).arc((-61,-42),(-63,-43)).assemble().finalize().extrude(-24))