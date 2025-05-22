import cadquery as cq
w0=cq.Workplane('YZ',origin=(-66,0,0))
r=w0.sketch().segment((-100,-85),(-11,-85)).segment((-23,-79)).segment((-7,-45)).segment((100,-45)).segment((100,-36)).segment((-2,-36)).segment((25,22)).segment((57,7)).segment((57,85)).segment((-100,85)).close().assemble().finalize().extrude(132)