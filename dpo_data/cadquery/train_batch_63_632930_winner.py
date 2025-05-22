import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-49,0))
w1=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().segment((-59,43),(-41,43)).arc((-35,42),(-29,43)).segment((-3,43)).segment((-3,58)).segment((-9,58)).arc((-35,100),(-61,58)).segment((-59,58)).close().assemble().push([(-27,51)]).circle(2,mode='s').finalize().extrude(40).union(w0.sketch().push([(-47,-79)]).rect(34,42).push([(-35.5,-70)]).rect(9,6,mode='s').finalize().extrude(85)).union(w1.sketch().segment((-18,45),(49,45)).segment((49,55)).segment((-11,55)).arc((-14,64),(-18,55)).close().assemble().finalize().extrude(56))