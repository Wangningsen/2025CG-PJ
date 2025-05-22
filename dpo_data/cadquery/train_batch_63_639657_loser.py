import cadquery as cq
w0=cq.Workplane('YZ',origin=(-66,0,0))
r=w0.sketch().segment((-100,-85),(-11,-85)).segment((-22,-80)).segment((16,9)).segment((57,9)).segment((57,85)).segment((-100,85)).close().assemble().reset().face(w0.sketch().segment((4,-45),(100,-45)).segment((100,-36)).segment((11,-36)).close().assemble()).finalize().extrude(132)