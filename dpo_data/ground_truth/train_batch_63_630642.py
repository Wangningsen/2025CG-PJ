import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-82))
r=w0.sketch().segment((-23,-40),(-18,-41)).segment((-18,-100)).segment((18,-100)).segment((18,18)).segment((23,40)).segment((18,41)).segment((18,100)).segment((-18,100)).segment((-18,-18)).close().assemble().finalize().extrude(165)