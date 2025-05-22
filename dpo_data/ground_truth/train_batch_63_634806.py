import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-6,37),(48,33)).segment((48,35)).segment((-6,40)).close().assemble().finalize().extrude(-200).union(w0.sketch().arc((0,-45),(7,-28),(24,-36)).arc((-19,42),(0,-45)).assemble().finalize().extrude(-139))