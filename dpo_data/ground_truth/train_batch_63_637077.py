import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
w1=cq.Workplane('ZX',origin=(0,51,0))
r=w0.sketch().push([(17,0)]).circle(83).push([(5,-80)]).circle(2,mode='s').finalize().extrude(31).union(w1.sketch().push([(0,-12)]).circle(12).reset().face(w1.sketch().segment((-4,-22),(4,-22)).segment((4,-19)).segment((5,-19)).segment((5,-15)).segment((4,-15)).segment((4,-1)).segment((-4,-1)).segment((-4,-15)).segment((-4,-19)).close().assemble(),mode='s').finalize().extrude(-151))