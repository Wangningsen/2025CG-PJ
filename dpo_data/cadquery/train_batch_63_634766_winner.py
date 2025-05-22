import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-18))
w1=cq.Workplane('ZX',origin=(0,53,0))
r=w0.sketch().segment((-63,-43),(-60,-43)).segment((-63,-41)).close().assemble().finalize().extrude(118).union(w1.sketch().segment((-70,-92),(46,-92)).segment((46,-65)).arc((76,0),(46,65)).segment((46,92)).segment((-70,92)).segment((-70,65)).arc((-100,0),(-70,-65)).close().assemble().finalize().extrude(-106))