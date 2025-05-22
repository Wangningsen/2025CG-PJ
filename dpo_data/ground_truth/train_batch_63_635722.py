import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.workplane(offset=-43/2).moveTo(5.5,71.5).box(15,57,43).union(w0.sketch().segment((-42,-100),(-29,-100)).arc((-33,-64),(-2,-45)).segment((-2,-44)).segment((-1,-44)).segment((-1,-45)).arc((11,-47),(22,-55)).segment((22,-13)).segment((-42,-13)).close().assemble().finalize().extrude(77)).union(w1.sketch().push([(-38.5,39.5)]).rect(55,5).push([(-12.5,38.5)]).rect(3,3,mode='s').finalize().extrude(81))