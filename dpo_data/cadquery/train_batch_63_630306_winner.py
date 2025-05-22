import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-91))
r=w0.sketch().push([(-37,70)]).circle(30).reset().face(w0.sketch().segment((-39,-30),(-38,-40)).segment((31,-19)).segment((30,-10)).close().assemble()).finalize().extrude(-8).union(w0.sketch().segment((8,-88),(63,-100)).segment((67,-84)).segment((12,-71)).arc((12,-80),(8,-88)).assemble().finalize().extrude(190))