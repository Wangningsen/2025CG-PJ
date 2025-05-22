import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-90))
r=w0.sketch().push([(-37,70)]).circle(30).reset().face(w0.sketch().segment((-40,-40),(32,-20)).segment((30,-12)).segment((-39,-31)).arc((-39,-35),(-40,-40)).assemble()).finalize().extrude(-8).union(w0.sketch().segment((8,-88),(63,-100)).segment((67,-84)).segment((12,-71)).arc((12,-80),(8,-88)).assemble().finalize().extrude(189))